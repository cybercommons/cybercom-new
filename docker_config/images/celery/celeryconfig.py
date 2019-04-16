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

BROKER_URL = os.environ.get('BROKER_URL')
BROKER_USE_SSL = setBrookerSSL()
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') 
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": os.environ.get('MONGO_DB',"cybercom"),
    "taskmeta_collection": os.environ.get('MONGO_TOMBSTONE_COLLECTION',"tombstone")
}

CELERY_IMPORTS = tuple(os.environ.get('CELERY_IMPORTS').split(','))
