import ssl
# All broker and mongo information must correspond to Celery Broker and REST API
# This is an example with no connections placed within this file. <variable_name> 
# Please use the single node cookiecutter and copy celery/code to make sure everything matches!
BROKER_URL = 'amqp://<broker_user>:<broker_password>@<broker_host>:<broker_port>/<broker_vhost>'
BROKER_USE_SSL = {
    'keyfile': '<path_to_key.pem>',
    'certfile': '<path_to_cert.pem>',
    'ca_certs': '<path_to_cacert.pem>',
    'cert_reqs': ssl.CERT_REQUIRED
}
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://<mongo_host>:<mongo_port>/?ssl=true&ssl_ca_certs=<path_to_cacert.pem>&ssl_certfile=<path_to_cert.pem>"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "<application_short_name>",
    "taskmeta_collection": "tombstone"
}
#If you are pip installing the requirements.txt. It has the cybercomq repo. Example add task!
CELERY_IMPORTS = ("<github repo queue - example (cybercomq)>",)

#The cybercomq install url would be included in the requirements.txt
