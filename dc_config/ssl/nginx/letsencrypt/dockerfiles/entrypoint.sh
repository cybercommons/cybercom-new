#!/bin/bash

if [ -z "$NOTIFY_EMAIL" ];
  then 
   echo "Email address must be set for letsencrypt in cybercom_config.env"
   exit 0
fi 

if [ ! -d /etc/letsencrypt/renewal ];
  then
    certbot certonly --webroot -w /data/letsencrypt --email $NOTIFY_EMAIL --agree-tos --no-eff-email -d $FULL_QUALIFIED_DOMAIN_NAME
else
    certbot renew --noninteractive --quiet
fi
