console.log("MongoDB server init.js file");
// Connect to the MongoDB server
conn = new Mongo();

// Specify the database to use (e.g., "companiesdatabase")
// here, companiesdatabase is hardcoded and not loaded from .env file
db = conn.getDB("companiesdatabase");

// Load data from the main_company.json file directly into a variable
var fs = require('fs');
var jsonData = fs.readFileSync('/docker-entrypoint-initdb.d/main_company.json', 'utf8');

var data = JSON.parse(jsonData);

// Insert the data into the "companies" collection
db.companies.insert(data);

console.log("Data from main_company.json inserted successfully.");
