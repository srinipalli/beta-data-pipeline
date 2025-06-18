#!/bin/bash

# Load variables from .env
set -o allexport
source .env
set +o allexport

# Use default 'mysql' if no custom path is given
MYSQL=${MYSQL_CLIENT_PATH:-mysql}

# Run the SQL file
$MYSQL --local-infile=1 -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" < sqlfilesadded/create.sql
if [ $? -eq 0 ]; then
    echo "All records created successfully :)"
else
    echo "Failed to create records :("
fi
