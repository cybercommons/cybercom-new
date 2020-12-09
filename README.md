Cybercommons API 
=======

## DEVELOPMENTAL AT THIS POINT!!!


The Cybercommons framework is a Django Rest Framework API. The API leverages MongoDB to provide a Catalog and Data Store for storing metadata and data within a JSON document database. The API also includes Celery which is an asynchronous task queue/job queue based on distributed message passing.

DEVELOPMENTAL AT THIS POINT! This is not an offical release. Please experiment and provide Github Issues or a  Pull Request with added enhancements. 


## Requirements

* Docker
* Docker Compose
    * `pip install docker-compose`
* GNU Make or equivalent

## Installation

1. Edit values within dc_config/cybercom_config.env
2. Copy secrets_template.env into secrets.env under the same folder and add required credentials into it. 
3. Initialize database and generate internal SSL certs

        $ make init

4. Build and Deploy on local system.

        $ make build
        $ make superuser
        $ make run

5. API running http://localhost
    * Admin credentials set from above `make superuser` 

6. Kill

        $ make stop


### To run cybercommons on servers with a valid domain name.

## Installation

1. Edit values within dc_config/cybercom_config.env[FULL_QUALIFIED_DOMAIN_NAME,NOTIFY_EMAIL(These values must be set).
2. Copy secrets_template.env into secrets.env under the same folder and add required credentials into it.
3. Initialize database and generate internal SSL certs

        $ make init
4. Initialize and Get TLS certificates from LetsEncrypt
        
        $ make init_certbot

5. Build and Deploy on local system.

        $ make build
        $ make superuser
        $ make run_with_certbot

6. API running https://{domain-name-of-server}
    * Admin credentials set from above `make superuser`

7. Kill

        $ make stop


## TODO

1. JWT PAY-LOAD
2. Integration with Kubernetes
