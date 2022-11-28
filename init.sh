#!/bin/sh

# Credits
# echo "Credits to : Marc Partensky, Alexandre Bigot et Étienne Favière"
# echo --------
# echo

# Helper functions
random() {
    echo "$RANDOM `date +%s`" | sha256sum | base64 | head -c 32
}
scrap_domain_name() {
    dig -x `curl -sLq https://ipconfig.io` | grep PTR | grep -v ";" | awk '{print $NF}' | sed 's/.$//'
}


# Default values
domain_name=`scrap_domain_name`
postgres_user=`random`
postgres_password=`random`
postgres_db=frhack
postgres_host=postgres
postgres_port=5432
registry=marcpartensky
node_env=production
front_port=80
postgres_exposed_port=5432
network_name=web
network_external=false

# Prompt
echo "Let the default value if you don't know"
read -e -p "- Domain name: " -i $domain_name domain_name
read -e -p "- PostgreSQL exposed port: " -i $postgres_exposed_port postgres_exposed_port
read -e -p "- PostgreSQL username: " -i $postgres_user postgres_user
read -e -p "- PostgreSQL password: " -i $postgres_password postgres_password
read -e -p "- PostgreSQL database name: " -i $postgres_db postgres_db
read -e -p "- Node env: " -i $node_env node_env
read -e -p "- Docker registry: " -i $registry registry
read -e -p "- Docker external network: " -i $network_external network_external
if [ $network_external = "true" ]
then
    network_external=true
else
    network_external=false
fi
if [ $network_external ]
then
    read -e -p "- Docker external network name: " -i $network_name network_name
fi
export NETWORK_EXTERNAL=$network_external

env_path=./env
mkdir -p $env_path

# Output to .env
echo "# $env_path/postgres.env
POSTGRES_USER=$postgres_user
POSTGRES_DB=$postgres_db
POSTGRES_PASSWORD=$postgres_password
" > $env_path/postgres.env

echo "# $env_path/api.env
POSTGRES_USER=$postgres_user
POSTGRES_DB=$postgres_db
POSTGRES_PASSWORD=$postgres_password
POSTGRES_PORT=$postgres_port
POSTGRES_HOST=$postgres_host
" > $env_path/api.env

echo "# $env_path/pgweb.env
DATABASE_URL=postgres://$postgres_user:$postgres_password@$postgres_host:$postgres_port/$postgres_db?sslmode=disable
" > $env_path/pgweb.env

echo "# $env_path/front.env
NODE_ENV=$node_env
FRONT_PORT=80
API_URL=api.$domain_name
" > $env_path/front.env

echo "# $env_path/docker-compose.env
REGISTRY=$registry
DOMAIN_NAME=$domain_name
POSTGRES_EXPOSED_PORT=$postgres_exposed_port
NETWORK_NAME=$network_name
NETWORK_EXTERNAL=$network_external
" > $env_path/docker-compose.env

# Display
echo 
echo --------
echo 

cat env/*
