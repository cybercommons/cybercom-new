#!/bin/bash

echo "Mounting s3fs to /mnt/"

/usr/bin/s3fs -f -o allow_other,umask=0077,mp_umask=0077,uid=1000,gid=1000 ${AWSBUCKETNAME} /mnt/ &

/app/startCeleryWorker

 



echo "I have started the celery worker"
