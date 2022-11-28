# Credits

STACK_NAME=frhack

credits:
	@echo ---------------------------------------------------------------
	@echo Credits to : Marc Partensky, Alexandre Bigot et Étienne Favière
	@echo ---------------------------------------------------------------
	@echo 

compose: setup
	docker-compose up -d
swarm: setup
	$(call setup_env,docker-compose)
	docker stack deploy -c docker-compose.yml $(STACK_NAME)

setup: credits env build
build: env
	docker-compose build

rm-stack:
	docker stack rm $(STACK_NAME)

env:
	./init.sh
clear:
	rm -rf ./env
reset: clear env

lab:
	jupyter-lab --ip 0.0.0.0 --collaborative --allow-root
front: anfr-front/node_modules
	npm --prefix anfr-front start
anfr-front/node_modules:
	npm --prefix anfr-front install

# helper
define setup_env
	$(eval ENV_FILE := env/$(1).env)
	@echo "Load $(ENV_FILE)"
	$(eval include env/$(1).env)
	$(eval export sed 's/=.*//' env/$(1).env)
endef

