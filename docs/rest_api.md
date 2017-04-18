RESTful API
============


### Task Execution (celery)


### Catalog and Data Store

The Catalog and Data Store are using the same logic and syntax for access and query language. The database which holds the information is MongoDB. MongoDB is a schemaless document noSQL database. The query language that the API deploys is the json representation of MongoDB.

#### API Return Data Structure

The API returns data in a consistent structure. 

* count: number if result records returned
* meta: page, page_size, pages
* next and previous: urls to page through data
* results: list of records return from API   

        {
            "count": 1, 
            "meta": {
                "page": 1, 
                "page_size": 50, 
                "pages": 1
            }, 
            "next": null, 
            "previous": null, 
            "results": [
            
            ]
        }

#### API URL Parameters

##### page_size: 

The page_size returns the available records up to page_size. If more records exist, the next url value will be deployed.

        ?page_size=100
        ?page_size=0

If page_size=0 API will return all records.

##### page:

The page variable will move to the page requested. If the page does not exist the last page will be shown.

##### format: 

1. api (Default) - Return type is HTML format
2. json - Return type is JSON format
3. jsonp - Return type is JSONP format
4. xml - Return type is xml format

        https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/?format=json
        https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/.json

##### query:

The query url parameter holds the JSON format query language. Please see below


#### Query Language

The API query language is based from the [MongoDB pyhton query](https://docs.mongodb.com/manual/tutorial/query-documents/#python) syntax.

##### Create Database and Collections



visual

        https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/?format=json
        https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/.json    
