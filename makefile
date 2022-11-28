# Credits

STACK_NAME=frhack

help:                                 ## Show this help.
	@echo Makefile helper:
	@echo ----------------
	@grep -Fh "##" $(MAKEFILE_LIST) | grep -Fv grep | sed -e 's/\\$$//' | sed -e 's/##//'

compose: setup                        ## Run with docker compose
	docker-compose up -d --force-recreate
swarm: setup                          ## Run with docker swarm
	$(call setup_env,docker-compose)
	docker stack deploy -c docker-compose.yml $(STACK_NAME)

rm-stack:                             ## Clear the swarm stack
	docker stack rm $(STACK_NAME)
compose-down:                         ## Remove docker compose containers with its volumes
	docker-compose down -v

setup: credits env build              ## Setup all the project
build: env                            ## Build the project
	docker-compose build
env:                                  ## Define the environment variables
	./init.sh
clear:                                ## Clear the environment variables
	rm -rf ./env
reset: clear env                      ## Reset the environment variables

lab:                                  ## Run the jupyter lab without docker
	jupyter-lab --ip 0.0.0.0 --collaborative --allow-root
front: anfr-front/node_modules        ## Run the front without docker
	npm --prefix anfr-front start
anfr-front/node_modules:              ## Install the front dependencies without docker
	npm --prefix anfr-front install

# helper
define setup_env
	$(eval ENV_FILE := env/$(1).env)
	@echo "Load $(ENV_FILE)"
	$(eval include env/$(1).env)
	$(eval export sed 's/=.*//' env/$(1).env)
endef

credits:                              ## Show the credits
	@echo ---------------------------------------------------------------
	@echo Credits to : Marc Partensky, Alexandre Bigot et Étienne Favière
	@echo ---------------------------------------------------------------
	@echo 

