# TAIGA BIBBOX application

This container can be installed as [BIBBOX APP](http://bibbox.readthedocs.io/en/latest/admin-documentation/ "BIBBOX App Store") or standalone. 

* initial user/passwordd: **admin / 123123**
* after the docker installation follow these [instructions](https://github.com/bibbox/app-taiga/blob/master/INSTALL-APP.md)

## Standalone Installation

Clone the github repsoitory and start the install.sh. If necessary change the ports and volume mounts in `docker-compose.yml`.  

`sudo git clone https://github.com/bibbox/app-taiga

`sudo chmod +x install.sh`

`sudo ./install.sh`


## Install within BIBBOX

The BIBBOX framework can be installed 
* as a [virtual machine](http://bibbox.bbmri-eric.eu/resources/machine/), 
* using [vagrant/puppet](http://bibbox.readthedocs.io/en/latest/installation-vagrant/) 
* are on any Ubuntu System following these [instructions](http://bibbox.readthedocs.io/en/latest/installation-source/)  


## Docker Images Used
* [bibbox/taiga-front](https://hub.docker.com/r/bibbox/taiga-front) 
* [bibbox/taiga-back](https://hub.docker.com/r/bibbox/taiga-back) 
* [bibbox/taiga-proxy](https://hub.docker.com/r/bibbox/taiga-proxy) 
* [bibbox/taiga-rabbit](https://hub.docker.com/r/bibbox/taiga-rabbit) 
* [bibbox/taiga-event](https://hub.docker.com/r/bibbox/taiga-event) 
* [bitnami/redis:5.0](https://hub.docker.com/r/bitnami/redis), offical container
* [postgres:11-alpine](https://hub.docker.com/_/postgres), offical container
* [adminer](https://hub.docker.com/_/adminer), offical container

This Taiga Docker is mainly inspired by [docker-taiga](https://github.com/docker-taiga) with input from [evinsolutions](https://github.com/devinsolutions/docker-taiga).


### Documentation

* [Offical TIAGA Documentation](http://taigaio.github.io/taiga-doc/dist/)
* [TAIGA FAQ](http://taigaio.github.io/taiga-doc/dist/setup-faqs.html)
* [Upgrade Information (non docker](http://taigaio.github.io/taiga-doc/dist/upgrades.html)

## Install Environment Variables

* DOMAIN
* SECRET_PHRASE
* REDIS_PASSWORD
* RABBIT_PASSWORD
* DATABASE_PASSWORD

## Mounted Volumes

* data/conf/proxy
* data/conf/back
* data/conf/front
* data/db
* data/media


