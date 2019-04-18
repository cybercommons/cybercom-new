Cybercommons API 
=======

DEVELOPMENTAL AT THIS POINT!!!


## Requirements

* Docker
* Docker Compose
    * `pip install docker-compose`

## Installation

1. Initialize

        $ git clone <git repo url>
        $ cd ceybercommons/dc_config
        $ ./initializeCybercomDB

2. Edit values within dc_config/cybercom_config.env
3. Build and Deploy

        $ docker-compose build
        $ docker-compose up -d 


## TO DO

1. SSL Creation - current config with preset SSL 
2. JWT PAY-LOAD
3. Integration with Kubernetes
