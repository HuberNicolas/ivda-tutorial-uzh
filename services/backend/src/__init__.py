import os

import pandas as pd
from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restx import Api, Resource
from pymongo.collection import Collection
from statsmodels.tsa.ar_model import AutoReg

from .model import Company

# Configure Flask & Flask-PyMongo:
app = Flask(__name__)
# allow access from any frontend
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})
# MongoDB URI; defaults to a local MongoDB, overridden in Docker Compose
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/companiesdatabase")
pymongo = PyMongo(app)
# Get a reference to the companies collection.
companies: Collection = pymongo.db.companies
api = Api(app)


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"status": "ok"}


class CompaniesList(Resource):
    def get(self, args=None):
        # retrieve the arguments and convert to a dict
        args = request.args.to_dict()
        # If the user does not specify any category we retrieve all companies
        if args.get("category", "All") == "All":
            cursor = companies.find()
        # In any other case, we only return the companies where the category applies
        else:
            cursor = companies.find({"category": args["category"]})
        # we return all companies as json
        return [Company(**doc).to_json() for doc in cursor]


class Companies(Resource):
    def get(self, id):
        # search for the company by ID
        cursor = companies.find_one_or_404({"id": id})
        company = Company(**cursor)
        # retrieve args
        args = request.args.to_dict()
        algorithm = args.get("algorithm", "none")
        # retrieve the profit
        profit = company.profit
        # add to df
        profit_df = pd.DataFrame(profit).iloc[::-1].reset_index(drop=True)
        if algorithm == "random":
            # retrieve the profit value from 2021
            prediction_value = int(profit_df["value"].iloc[-1])
            # add the value to profit list at position 0
            company.profit.insert(0, {"year": 2022, "value": prediction_value})
        elif algorithm == "regression":
            # create model
            model_ag = AutoReg(endog=profit_df["value"], lags=1, trend="c", seasonal=False)
            # train the model
            fit_ag = model_ag.fit()
            # predict for 2022 based on the profit data
            prediction_value = fit_ag.predict(start=len(profit_df), end=len(profit_df), dynamic=False).iloc[0]
            # add the value to profit list at position 0
            company.profit.insert(0, {"year": 2022, "value": float(prediction_value)})
        return company.to_json()


api.add_resource(CompaniesList, "/companies")
api.add_resource(Companies, "/companies/<int:id>")
