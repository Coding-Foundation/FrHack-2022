# Credits

STACK_NAME=frhack

help:                                 ## show this help.
	@echo Makefile helper:
	@echo ----------------
	@grep -Fh "##" $(MAKEFILE_LIST) | grep -Fv grep | sed -e 's/\\$$//' | sed -e 's/##//'

compose: setup                        ## run with docker compose
	docker-compose up -d
swarm: setup                          ## run with docker swarm
	$(call setup_env,docker-compose)
	docker stack deploy -c docker-compose.yml $(STACK_NAME)

setup: credits env build              ## setup all the project
build: env                            ## build the project
	docker-compose build

rm-stack:                             ## clear the swarm stack
	docker stack rm $(STACK_NAME)

env:                                  ## define environment variables
	./init.sh
clear:                                ## clear environment variables
	rm -rf ./env
reset: clear env                      ## reset envrionment variables

lab:                                  ## run jupyter lab without docker
	jupyter-lab --ip 0.0.0.0 --collaborative --allow-root
front: anfr-front/node_modules        ## run front without docker
	npm --prefix anfr-front start
anfr-front/node_modules:              ## install front dependencies without docker
	npm --prefix anfr-front install

# helper
define setup_env
	$(eval ENV_FILE := env/$(1).env)
	@echo "Load $(ENV_FILE)"
	$(eval include env/$(1).env)
	$(eval export sed 's/=.*//' env/$(1).env)
endef

credits:                              ## show credits
	@echo ---------------------------------------------------------------
	@echo Credits to : Marc Partensky, Alexandre Bigot et Étienne Favière
	@echo ---------------------------------------------------------------
	@echo 

