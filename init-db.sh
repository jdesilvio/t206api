#!/bin/bash
set -e

echo "Creating T206 database"

psql <<- EOSQL
    CREATE USER t206admin;
    CREATE DATABASE t206db;
    GRANT ALL PRIVILEGES ON DATABASE t206db TO t206admin;
EOSQL
