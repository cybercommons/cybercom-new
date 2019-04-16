__author__ = 'cyberCommons Framework'

import os
import ssl
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ****** Application Settings *******************************************************

APPLICATION_TITLE = os.environ.get('APPLICATION_TITLE','Cybercommons')

# ******* Backend Communication Celery Brooker and MongoDB **************************

MEMCACHE_HOST = "cybercom_memcache"
MEMCACHE_PORT = 11211

# Celery workers config are setup with the folling DB and Collections
# Change would reqire updating celeryconfig.py within celery image folder
MONGO_DB = os.environ.get('MONGO_DB',"cybercom")
MONGO_LOG_COLLECTION = os.environ.get('MONGO_LOG_COLLECTION',"task_log")
MONGO_TOMBSTONE_COLLECTION = os.environ.get('MONGO_TOMBSTONE_COLLECTION',"tombstone")

SSL_PATH=os.environ.get('SSL_PATH','{0}/docker_config/ssl/backend'.format(BASE_DIR))
BROKER_URL = os.environ.get('BROKER_URL','amqp://quser:RJAkDsP7UkW9@cybercom_rabbitmq:5671/vhost')
BROKER_USE_SSL = {
    'keyfile': '{0}/client/key.pem'.format(SSL_PATH),
    'certfile': '{0}/client/cert.pem'.format(SSL_PATH),
    'ca_certs': '{0}/testca/cacert.pem'.format(SSL_PATH),
    'cert_reqs': ssl.CERT_REQUIRED
}

MONGO_URI = os.environ.get('MONGO_URI','mongodb://quser:RJAkDsP7UkW9@cybercom_mongo:27017/?ssl=true&ssl_ca_certs={0}/testca/cacert.pem&ssl_certfile={0}/client/mongodb.pem'.format(
    SSL_PATH))
CELERY_RESULT_BACKEND = MONGO_URI
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

# ******* Catalog ******************************************************
CATALOG_EXCLUDE = ['admin','config', 'local', MONGO_DB]
CATALOG_INCLUDE = ['catalog']
CATALOG_URI = MONGO_URI
CATALOG_ANONYMOUS = True
# *********** Data Store ************************************************
DATA_STORE_EXCLUDE = ['admin','config', 'local', MONGO_DB,'catalog']
DATA_STORE_MONGO_URI = MONGO_URI
DATA_STORE_ANONYMOUS = True


# *********** Email Configuration ********************
# Uncomment and configure to enable send email
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'username'
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_USE_TLS = True
