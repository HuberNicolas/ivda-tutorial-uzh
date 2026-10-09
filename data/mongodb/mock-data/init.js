// Runs once, when MongoDB starts with an empty data volume.
// Loads the mock companies from main_company.json into the "companies" collection.
const fs = require("fs");

const dbName = process.env.MONGO_INITDB_DATABASE || "companiesdatabase";
const companiesDb = db.getSiblingDB(dbName);

const data = JSON.parse(fs.readFileSync("/docker-entrypoint-initdb.d/main_company.json", "utf8"));
companiesDb.companies.insertMany(data);

print(`Inserted ${data.length} companies into ${dbName}.companies`);
