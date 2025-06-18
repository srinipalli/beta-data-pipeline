#!/bin/bash

# Exit immediately on error
set -e

echo "Loading environment variables..."
set -o allexport
source .env
set +o allexport

# Use default mysql if not provided
MYSQL=${MYSQL_CLIENT_PATH:-mysql}

echo "Using MySQL binary: $MYSQL"
echo "Database: $MYSQL_DATABASE"
echo "User: $MYSQL_USER"

# Execute SQL
echo "Running SQL file..."
$MYSQL --local-infile=1 -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" < sqlfilesadded/deleteall.sql

if [ $? -eq 0 ]; then
    echo "✅ All records deleted successfully."
else
    echo "🟥 Failed to delete records."
fi