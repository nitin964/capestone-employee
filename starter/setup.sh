#!/bin/bash
export DATABASE_URL="postgresql://postgres:admin@localhost:5432/postgres"
export AUTH0_DOMAIN="dev-qhqw-viy.us.auth0.com"
export ALGORITHMS="['RS256']"
export API_AUDIENCE="employee"
echo "setup.sh script executed successfully!"