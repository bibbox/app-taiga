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
* [dockertaiga/front](https://hub.docker.com/r/dockertaiga/front) 
* [dockertaiga/back](https://hub.docker.com/r/dockertaiga/back) 
* [dockertaiga/proxy](https://hub.docker.com/r/dockertaiga/proxy) 
* [dockertaiga/rabbit](https://hub.docker.com/r/dockertaiga/rabbit) 
* [dockertaiga/event](https://hub.docker.com/r/dockertaiga/event) 
* [bitnami/redis:5.0](https://hub.docker.com/r/bitnami/redis), offical container
* [postgres:11-alpine](https://hub.docker.com/_/postgres), offical container
* [adminer](https://hub.docker.com/_/adminer), offical container

for an alternatiev TAIGA docker and hints on more configuration varaibels  hav a look at [evinsolutions] repository (https://github.com/devinsolutions/docker-taiga) 

* https://github.com/docker-taiga
* https://github.com/devinsolutions/docker-taiga


## Install Environment Variables

* DOMAIN
* DATABASE_PASSWORD

## Mounted Volumes

* data/conf
* data/db

