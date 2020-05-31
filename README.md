# TAIGA BIBBOX application

## Hints
* approx. time with medium fast internet connection: **5 minutes**
* initial user/passwordd: **admin / 123123 **


## Docker Images Used
* [dockertaiga/front](https://hub.docker.com/r/dockertaiga/front) 
* [dockertaiga/back](https://hub.docker.com/r/dockertaiga/back) 
* [dockertaiga/proxy](https://hub.docker.com/r/dockertaiga/proxy) 
* [dockertaiga/rabbit](https://hub.docker.com/r/dockertaiga/rabbit) 
* [dockertaiga/event](https://hub.docker.com/r/dockertaiga/event) 
* [bitnami/redis:5.0](https://hub.docker.com/r/bitnami/redis), offical container
* [postgres:11-alpine](https://hub.docker.com/_/postgres), offical container
* [adminer](https://hub.docker.com/_/adminer), offical container

for an alternatiev TAIGA docker and hints on more configuration varaibels  hav a look at [evinsolutions] repository (https://github.com/devinsolutions/docker-taiga) 


## Install Environment Variables

* DOMAIN
* DATABASE_PASSWORD

## Mounted Volumes

* data/conf
* data/db

