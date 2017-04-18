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

1. Install Python's virtualenv :sub:`~` $ pip install virtualenv
   :sub:`~`
2. Create virtual environment and activate :sub:`~` $ virtualenv virtpy
   $ source virtpy/bin/activate :sub:`~`
3. Install Celery :sub:`~` (virtpy) $ pip install Celery :sub:`~`

Configuration
~~~~~~~~~~~~~

Get Config Files and Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download example celeryconfig.py and requirements.txt :sub:`~` $ wget
   https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery\_worker/celeryconfig.py
   $ wget
   https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery\_worker/requirements.txt
   :sub:`~`

2. Create SSL directory and copy cyberCommon's client certificates
   :sub:`~` $ mkdir ssl $ cp mongodb.pem ssl/ $ cp key.pem ssl/ $ cp
   cert.pem ssl/ $ cp cacert.pem ssl/ :sub:`~`

3. Configure celeryconfig.py to point to client certificates and use
   corresponding credentials :sub:`~` BROKER\_URL =
   'amqp://username:password@:/' BROKER\_USE\_SSL = { 'keyfile':
   'ssl/key.pem', 'certfile': 'ssl/cert.pem', 'ca\_certs':
   'ssl/cacert.pem', 'cert\_reqs': ssl.CERT\_REQUIRED }
   :sub:`:sub:`:sub:` ``` CELERY\_RESULT\_BACKEND =
   "mongodb://username:password@:/?ssl=true&ssl\_ca\_certs=ssl/cacert.pem>&ssl\_certfile=mongodb.pem>"
   :sub:`~`

Configure Tasks
^^^^^^^^^^^^^^^

1. Update requirements.txt to include desired libraries and task
   handlers.
2. Update celeryconfig.py to import task handlers that have been
   included in requirements file. :sub:`~` CELERY\_IMPORTS =
   ("cybercomq", "name\_of\_additional\_task\_handler\_library", )
   :sub:`~`
3. Install requirements :sub:`~` (virtpy) $ pip install -r
   requirements.txt :sub:`~`

Launch Celery worker
~~~~~~~~~~~~~~~~~~~~

-  Run in foreground :sub:`~` $ celery worker -l info -Q remote -n
   dev-mstacy1 :sub:`~`
