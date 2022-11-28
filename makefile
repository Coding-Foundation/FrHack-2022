# Credits

STACK_NAME=frhack

help:                                 ## Show this help.
	@echo Makefile helper:
	@echo ----------------
	@grep -Fh "##" $(MAKEFILE_LIST) | grep -Fv grep | sed -e 's/\\$$//' | sed -e 's/##//'

compose: setup                        ## Run with docker compose
	./run.sh docker-compose up -d --force-recreate
swarm: setup                          ## Run with docker swarm
	./run.sh docker stack deploy -c docker-compose.yml $(STACK_NAME)

rm-stack:                             ## Clear the swarm stack
	./run.sh docker stack rm $(STACK_NAME)
compose-down:                         ## Remove docker compose containers
	./run.sh docker-compose down -v

setup: credits env build              ## Setup the project
build: env                            ## Build the project
	./run.sh docker-compose build --pull
# NETWORK_NAME=$(NETWORK_NAME) env | grep NETWORK_NAME
env:                                  ## Define the environment variables
	./init.sh
rm-env:                               ## Remove the environment variables
	rm -rf ./env
rm-volume:                            ## Remove docker compose volumes
	./run.sh docker volume rm $(STACK_NAME)_postgres_frhack || true
clear: rm-env rm-volume
reset: clear env                     ## Reset the environment variables

lab:                                  ## Run the jupyter lab without docker
	jupyter-lab --ip 0.0.0.0 --collaborative --allow-root
front: anfr-front/node_modules        ## Run the front without docker
	npm --prefix anfr-front start
anfr-front/node_modules:              ## Install the front dependencies without docker
	npm --prefix anfr-front install

credits:                              ## Show the credits
	@echo ---------------------------------------------------------------
	@echo Credits to : Marc Partensky, Alexandre Bigot and Étienne Favière
	@echo ---------------------------------------------------------------
	@echo 

