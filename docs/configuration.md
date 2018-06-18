System Configuration
==================

### Generating SSL Keys and Where They are Stored
Rabbitmq and MongoDB are configured to use SSL certificates to secure their communications. By default, during the setup of cyberCommons, these certificates are configured to be valid for 365 days. Once the certificates expire, they will need to be regenerated. If the ssl self-signed option was selected during installation, the certificates generated for the web server (NGINX) will also expire at this time and will need to be regenerated.

#### Generating SSL certificates
  Self-signed certificates are automatically generated on first run for RabbitMQ and MongoDB. Self-signed certificates for NGINX will be generated automatically during configuration if the self-signed option was selected during configuration.

  LetsEncrypt - refer to the [LetsEncrypt](installation.html#build-let-s-encrypt-docker-container) section of the installation instructions.

#### Renewing SSL Certificates
  1. Self-signed certificates can be updated by running the following command from the cyberCommons root directory:

  	$ run/genSSLKeys


  *All remote Celery workers will need the new SSL client certificates to resume communications. See the section below on where these certificates are stored*

  1. LetsEncrypt certificates can be renewed by running the following from the cyberCommons root directory:
  ~~~~
  $ config/ssl/nginx/runLetsEncrypt
  ~~~~

  *Follow LetsEncrypt's prompts*

#### SSL Certificate Locations
  1. Self-signed locations:
     * MongoDB
       - config/ssl/backend/client/mongodb.pem
       - config/ssl/backend/server/mongodb.pem
       - config/ssl/testca/cacert.pem
     * NGINX
       - config/ssl/nginx/keys/dhparam.pem
       - config/ssl/nginx/keys/selfsigned.crt
       - config/ssl/nginx/keys/selfsigned.key
     * RabbitMQ
       - config/ssl/backend/client/key.pem
       - config/ssl/backend/client/cert.pem
       - config/ssl/backend/server/key.pem
       - config/ssl/backend/server/cert.pem
       - config/ssl/testca/cacert.pem

  1. LetsEncrypt location:
     * NGINX
       - config/ssl/nginx/keys/dhparam.pem
       - config/ssl/nginx/letcencrypt/etc/live/*

### Configure Email Backend
* Uncomment and configure the Email Configuration section in config/api_config.py. *The following is an example using gmail.*
~~~
#*********** Email Configuration ********************
# Uncomment and configure to enable send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
~~~

* To enable Admin email notifications, add a line similar to the following to the config/api_config.py file. *Refer to Django's [documentation](https://docs.djangoproject.com/en/1.8/topics/email/) for more details on configuring email.*
~~~
ADMINS = [('Jane', 'ccadmin@your.org'), ('John', 'ccadmin2@your.org')]
~~~

### Add Admin User to MongoDB
1. Uncomment and configure the following section in the config/config.sh file. *Refer to MongoDB's [documentation](https://docs.mongodb.com/manual/reference/built-in-roles/) for more details on built-in-roles.*
~~~
# uncomment and populate the following two lines for the resetDBCreds application to add / update the mongo user admin account
mongo_admin_username=<adminuser>
mongo_admin_password=<use_strong_password>
mongo_admin_role=root
~~~

1. Run the following command from cyberCommons' root directory. *This step will restart the MongoDB server and create or update the admin user.*
~~~
$ run/resetDBCreds
~~~

### Open RabbitMQ and MongoDB Ports for Remote Workers
1. Edit run/cybercom_up with the following changes
  * Edit MongoDB config to include port 27017
  ~~~
  docker run -d -p 27017:27017 --name example_mongo \
  ~~~

  * Edit RabbitMQ config to include port 5671
  ~~~
  #Rabbitmq
  echo "************** Rabbitmq        ***********"
  docker run -d -p 5671:5671 --name example_rabbitmq \
  ~~~
1. Update firewall rules on host to allow access to these ports

### Turn Off Debug Mode for RESTful API
1. Set DEBUG = False in config/api_config.py
1. Add host(s) to ALLOWED_HOSTS list. See Django's documentation on the [ALLOWED_HOSTS](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ALLOWED_HOSTS) setting for more detail.
