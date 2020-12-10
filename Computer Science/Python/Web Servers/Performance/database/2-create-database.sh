#!/bin/bash

TEST=`psql -U "$POSTGRES_USER" <<- EOSQL
   SELECT 1 FROM pg_database WHERE datname='$DB_NAME';
EOSQL`

if [[ $TEST == "1" ]]; then
# database exists
# $? is 0
echo ""
echo "****** DATABASE ALREADY EXISTS ******"
exit 0

else

echo ""
echo "****** CREATING DOCKER DATABASE ******"
psql -U "$POSTGRES_USER" <<- EOSQL
CREATE ROLE $DB_USER WITH LOGIN ENCRYPTED PASSWORD '${DB_PASS}' CREATEDB;
EOSQL

psql -U "$POSTGRES_USER" <<- EOSQL
   CREATE DATABASE $DB_NAME WITH OWNER $DB_USER TEMPLATE template0 ENCODING 'UTF8';
EOSQL

psql -U "$POSTGRES_USER" <<- EOSQL
   GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL

fi

echo ""
echo "****** DOCKER DATABASE CREATED ******"
