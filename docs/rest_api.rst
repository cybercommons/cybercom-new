RESTful API
===========

Catalog and Data Store
~~~~~~~~~~~~~~~~~~~~~~

The Catalog and Data Store are using the same logic and syntax for
access and query language. The database which holds the information is
MongoDB. MongoDB is a schemaless document noSQL database. The query
language that the API deploys is the json representation of MongoDB.

API Return Data Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

The API returns data in a consistent structure.

-  count: number if result records returned
-  meta: page, page\_size, pages
-  next and previous: urls to page through data
-  results: list of records return from API

   ::

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

API URL Parameters
^^^^^^^^^^^^^^^^^^

page\_size:
'''''''''''

The page\_size returns the available records up to page\_size. If more
records exist, the next url value will be deployed.

::

        ?page_size=100
        ?page_size=0

If page\_size=0 API will return all records.

page:
'''''

The page variable will move to the page requested. If the page does not
exist the last page will be shown.

format:
'''''''

1. api (Default) - Return type is HTML format
2. json - Return type is JSON format
3. jsonp - Return type is JSONP format
4. xml - Return type is xml format

   ::

       https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/?format=json
       https://cc.lib.ou.edu/api/catalog/data/catalog/digital_objects/.json

query:
''''''

The query url parameter is a JSON format query language. Please see
below

Query Language
^^^^^^^^^^^^^^

The API query language is based from the `MongoDB pyhton
query <https://docs.mongodb.com/manual/tutorial/query-documents/#python>`__
syntax.

Create Database and Collections
'''''''''''''''''''''''''''''''

Create Database
               

::

        View: /api/data_store/data/  HTTP Request: Post
        Data: {"database":"mydata"}  Format: JSON
        

Delete Database
               

::

        View: /api/data_store/data/  HTTP Request: Post
        Data: {"action":"delete","database":"mydata"}  Format: JSON        

Create Collection
                 

::

        View: /api/data_store/data/mydata  HTTP Request: Post
        Data: {"collection":"mycollection"}  Format: JSON

Delete Collection
                 

::

        View: /api/data_store/data/mydata  HTTP Request: Post
        Data: {"action":"delete","collection":"mycollection"}  Format: JSON

Filter Query
''''''''''''

The following examples are on the collection view.

Filter Query
            

::

        ?query={"filter":{"tag":"content"}}

        ?query={"filter":{"tag":"content","tag2":"content"}}
        
        # Return fields

        ?query={"filter":{"tag":"content","tag2":"content"},"projection":{"tag":0}

Distinct Query
''''''''''''''

::

        ?action=distinct&field=test
        # Include query parameter
        ?action=distinct&field=bag&query={"filter":{"department":"Informatics"}}

Group By Query
''''''''''''''

::

        ?action=groupby&groupby=department&variable=rate
        # Multiple fields in groupby and query field
        ?action=groupby&groupby=department,bag&variable=rate&query={"filter":{"department":"Informatics"}}

Task Execution (celery)
~~~~~~~~~~~~~~~~~~~~~~~

The Celery Distributed Task Queue is integrated throught the RESTful
API.

List of Available Tasks and Task History
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

        URL: /api/queue/
        Task History: /api/queue/usertasks/

Task Submission
^^^^^^^^^^^^^^^

::

        Example:
        URL /api/queue/run/cybercomq.tasks.tasks.add/
        Docstring: Very import to give users the description of task. 
        Curl Example: Comand-line example with API token
        

Task HTML POST Data Requirement
'''''''''''''''''''''''''''''''

::

        {
            "function": "cybercomq.tasks.tasks.add",
            "queue": "celery",
            "args": [],
            "kwargs": {},
            "tags": []
        }

function: task name queue: which queue to route the task args: [] List
of argument kwargs: {} Keyword arguments tags: [] list of tags that will
identify task run

Curl Command - Command-line Scripting
'''''''''''''''''''''''''''''''''''''

::

        curl -X POST --data-ascii '{"function":"cybercomq.tasks.tasks.add","queue":"celery","args":[],"kwargs":{  },"tags": []}' http://localhost/api/queue/run/cybercomq.tasks.tasks.add/.json -H Content-Type:application/json -H 'Authorization: Token < authorized-token > '

Python Script to Execute Script
'''''''''''''''''''''''''''''''

::

        import requests,json

        headers ={'Content-Type':'application/json',"Authorization":"Token < authorized token >"}
        data = {"function":"cybercomq.tasks.tasks.add","queue":"celery","args":[2,2],"kwargs":{},"tags":["add"]}
        req=requests.post("http://localhost/api/queue/run/cybercomq.tasks.tasks.add/.json",data=json.dumps(data),headers=headers) 
        print(req.text)

Javascript JQuery $.postJSON
''''''''''''''''''''''''''''

::

        $.postJSON = function(url, data, callback,fail) {
            return jQuery.ajax({
                'type': 'POST',
                'url': url,
                'contentType': 'application/json',
                'data': JSON.stringify(data),
                'dataType': 'json',
                'success': callback,
                'error':fail,
                'beforeSend':function(xhr, settings){
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            });
        }
