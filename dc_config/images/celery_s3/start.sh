#!/bin/bash

<<<<<<< HEAD
echo "Mounting s3fs to /mnt/"
=======
echo "hello world"

>>>>>>> parent of 982367d... imageMagick support added to the celery container && echo output changed in start shell script
/usr/bin/s3fs -f -o allow_other,umask=0077,mp_umask=0077,uid=1000,gid=1000 ${AWSBUCKETNAME} /mnt/ &

echo "Starting Celery worker"
/app/startCeleryWorker

