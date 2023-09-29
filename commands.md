# Part 0

node -v

npm -v

mkdir example-project

cd example-project

npm install -g @vue/cli

vue create hello-world
    -SELECT FIRST OPTION "Default ([Vue 3] babel, eslint)"

cd hello-world

npm install

npm run serve
    - AFTER 30seconds, press: "CTRL + C"

vue add vuetify
    - PRESS "y"
    - SELECT 5TH OPTION "Vuetify 3 - Vue CLI (preview)"

npm run serve

# Part 2

PRESS: "CTRL + C"

npm install plotly.js

npm run serve

# Part 3

PRESS: "CTRL + C"

mkdir services
mkdir services/frontend
mkdir services/backend

find ./example-project/hello-world -exec mv -n {} ./services/frontend \;
rm -rf ./example-project/hello-world
rm -rf ./example-project
cd /services/frontend
npm install

cd ../backend
python -m venv env
source env/bin/activate
(pip list)
pip install flask==2.1.1 pip install flask-restx==0.5.1 pip install werkzeug=2.1.2
(pip list)

mkdir src

python app.py run
curl -X GET http://127.0.0.1:5000/ping

# Part 4

pip install fastapi flask_pymongo pymongo flask_cors
deactivate # or conda deactivate