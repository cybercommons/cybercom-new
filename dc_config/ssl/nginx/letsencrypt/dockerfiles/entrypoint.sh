#!/bin/bash
set -e
if [ ! -f /etc/letsencrypt/renewal ]
  then
    certbot certonly --webroot -w /www -d localhost
  else
    certbot renew --noninteractive --quiet
fi
