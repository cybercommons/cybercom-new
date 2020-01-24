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
2. Initialize database and generate internal SSL certs

        $ make init

3. Build and Deploy

        $ make build
        $ make run

4. API running http://localhost:8080
    * Username: admin
    * Password: admincybercom

5. Kill

        $ make stop

## TODO

1. NGINX config 
2. JWT PAY-LOAD
3. Integration with Kubernetes
