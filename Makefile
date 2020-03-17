include dc_config/cybercom_config.env

COMPOSE_INIT = docker-compose -f dc_config/images/docker-compose-init.yml

.PHONY: init intidb initssl run stop restart_api

.EXPORT_ALL_VARIABLES:
UID=$(shell id -u)
GID=$(shell id -g)

init: 
	$(COMPOSE_INIT) build
	$(COMPOSE_INIT) up
	$(COMPOSE_INIT) down

initdb:
	$(COMPOSE_INIT) up cybercom_mongo_init
	$(COMPOSE_INIT) down

initssl:
	$(COMPOSE_INIT) build cybercom_openssl_init
	$(COMPOSE_INIT) up cybercom_openssl_init
	$(COMPOSE_INIT) down

build:
	@docker-compose build

run:
	@docker-compose up -d

stop:
	@docker-compose down

restart_api:
	@docker-compose restart cybercom_api

