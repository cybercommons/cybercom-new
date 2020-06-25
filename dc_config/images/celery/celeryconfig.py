import os
import ssl

def setBrookerSSL():
    if os.environ.get('BROKER_USE_SSL'):
        return {'keyfile': '/ssl/client/key.pem',
                'certfile': '/ssl/client/cert.pem',
                'ca_certs': '/ssl/testca/cacert.pem',
                'cert_reqs': ssl.CERT_REQUIRED}
    else:
        return None

# SETUP BROOKER URI
RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
RABBITMQ_DEFAULT_VHOST = os.environ.get('RABBITMQ_DEFAULT_VHOST')
BROKER_URL = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@cybercom_rabbitmq:5671/{RABBITMQ_DEFAULT_VHOST}"
BROKER_USE_SSL = setBrookerSSL()
CELERY_SEND_EVENTS = True
CELERY_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['json']

# SETUP MONGO URI
SSL_PATH = os.environ.get('SSL_PATH')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
CELERY_RESULT_BACKEND = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@cybercom_mongo:27017/?ssl=true&ssl_ca_certs={SSL_PATH}/testca/cacert.pem&ssl_certfile={SSL_PATH}/client/mongodb.pem" 

CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": os.environ.get('MONGO_DB', "cybercom"),
    "taskmeta_collection": os.environ.get('MONGO_TOMBSTONE_COLLECTION', "tombstone")
}

CELERY_IMPORTS = tuple(os.environ.get('CELERY_IMPORTS').split(','))
