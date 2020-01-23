initdb:
	@cd dc_config/images/mongoinit; docker-compose build
	@cd dc_config/images/mongoinit; docker-compose up
	@cd dc_config/images/mongoinit; docker-compose down
.PHONY: initdb

build:
	@docker-compose build

run:
	@docker-compose up -d
.PHONY: run

stop:
	@docker-compose down
.PHONY: stop

restart_api:
	@docker-compose restart cybercom_api
.PHONY: restart_api

