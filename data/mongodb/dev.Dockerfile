FROM mongo:latest
COPY ./mock-data/init.js /docker-entrypoint-initdb.d/init.js
COPY ./mock-data/main_company.json /docker-entrypoint-initdb.d/main_company.json