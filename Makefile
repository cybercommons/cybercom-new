include dc_config/cybercom_config.env
include dc_config/secrets.env

COMPOSE_INIT = docker-compose -f dc_config/images/docker-compose-init.yml

.PHONY: init intidb initssl dbshell dbexport dbimport run stop test restart_api init_certbot

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

superuser:
	@docker-compose run --rm cybercom_api ./manage.py createsuperuser 

init_certbot:
	@docker-compose -f dc_config/images/certbot-initialization.yml build
	@docker-compose -f dc_config/images/certbot-initialization.yml up --abort-on-container-exit
	@docker-compose -f dc_config/images/certbot-initialization.yml down

dbshell:
	@docker-compose exec cybercom_mongo mongo admin \
		--tls \
		--host cybercom_mongo \
		--tlsCertificateKeyFile /ssl/client/mongodb.pem \
		--tlsCAFile /ssl/testca/cacert.pem \
		--username $$MONGO_USERNAME \
		--password $$MONGO_PASSWORD

db ?= "catalog"
collection ?= "digital_objects"
dbexport:
	@docker-compose exec cybercom_mongo mongoexport \
		--quiet \
		--db=$(db) \
		--collection=$(collection) \
		--ssl \
		--host cybercom_mongo \
		--sslPEMKeyFile /ssl/client/mongodb.pem \
		--sslCAFile /ssl/testca/cacert.pem \
		--username $$MONGO_USERNAME \
		--password $$MONGO_PASSWORD

dbimport:
	@docker-compose exec -T cybercom_mongo mongoimport \
		--db=$(db) \
		--collection=$(collection) \
		--ssl \
		--host cybercom_mongo \
		--sslPEMKeyFile /ssl/client/mongodb.pem \
		--sslCAFile /ssl/testca/cacert.pem \
		--username $$MONGO_USERNAME \
		--password $$MONGO_PASSWORD

build:
	@docker-compose --compatibility build

run:
	@docker-compose --compatibility up -d

stop:
	@docker-compose --compatibility down

test:
	@tox -e django

restart_api:
	@docker-compose restart cybercom_api

collectstatic:
	@docker-compose run --rm cybercom_api ./manage.py collectstatic

