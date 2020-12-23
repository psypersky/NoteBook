#!/bin/bash

echo "****** Adding fixed data ******"

psql -U "$DB_USER" "$DB_NAME" -f /usr/fixed-data.sql

echo ""
echo "****** Fixed data added! ******"
