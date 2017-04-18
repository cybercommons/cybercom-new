Installation remote worker
==========================

cyberCommons can scale horizontally by allowing remote workers to take
on tasks and execute them on remote systems. The following describes how
to setup a remote `Celery <http://www.celeryproject.org/>`__ worker for
use with cyberCommons. Celery is focused on real-time operation, but
supports scheduling as well.

The execution units, called tasks, are executed concurrently on a single
or more worker servers using multiprocessing, Eventlet, or gevent. Tasks
can execute asynchronously (in the background) or synchronously (wait
until ready).

Requirements
~~~~~~~~~~~~

-  PIP -
   `Install <https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers>`__
-  Copies of client certificates to communicate with central
   cyberCommons server:
-  MongoDB

   -  config/ssl/backend/client/mongodb.pem
   -  config/ssl/testca/cacert.pem

-  RabbitMQ

   -  config/ssl/backend/client/key.pem
   -  config/ssl/backend/client/cert.pem
   -  config/ssl/testca/cacert.pem

Install Celery
~~~~~~~~~~~~~~

1. Install Python's virtualenv

::

   $ pip install virtualenv

2. Create virtual environment and activate

::

   $ virtualenv virtpy
   $ source virtpy/bin/activate

3. Install Celery

::

   (virtpy) $ pip install Celery

Configuration
~~~~~~~~~~~~~

Get Config Files and Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download example celeryconfig.py and requirements.txt

::

   $ wget https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery_worker/celeryconfig.py
   $ wget https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery_worker/requirements.txt

2. Create SSL directory and copy cyberCommon's client certificates

::

   $ mkdir ssl
   $ cp mongodb.pem ssl/
   $ cp key.pem ssl/
   $ cp cert.pem ssl/
   $ cp cacert.pem ssl/

3. Configure celeryconfig.py to point to client certificates and use
   corresponding credentials

::

   BROKER_URL = 'amqp://username:password@<broker_host>:<broker_port>/<broker_vhost>'
   BROKER_USE_SSL = {
     'keyfile': 'ssl/key.pem',
     'certfile': 'ssl/cert.pem',
     'ca_certs':  'ssl/cacert.pem',
     'cert_reqs': ssl.CERT\_REQUIRED
   }

::

   CELERY_RESULT_BACKEND = "mongodb://username:password@<mongo_host>:<mongo_port>/?ssl=true&ssl_ca_certs=ssl/cacert.pem>&ssl_certfile=mongodb.pem>"

Configure Tasks
^^^^^^^^^^^^^^^

1. Update requirements.txt to include desired libraries and task
   handlers.
2. Update celeryconfig.py to import task handlers that have been
   included in requirements file.

::

   CELERY_IMPORTS = ("cybercomq", "name_of_additional_task_handler_library", )

3. Install requirements

::

   (virtpy) $ pip install -r requirements.txt

Launch Celery worker
~~~~~~~~~~~~~~~~~~~~

-  Run in foreground

::

   $ celery worker -l info -Q remote -n dev-mstacy1
