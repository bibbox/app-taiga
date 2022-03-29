# TAIGA BIBBOX application

This container can be installed as [BIBBOX APP](http://bibbox.readthedocs.io/en/latest/admin-documentation/ "BIBBOX App Store") or standalone. 

* initial user/password: **admin / vendetta** 
* after the docker installation follow these [instructions](INSTALL-APP.md)

## Standalone Installation

Clone the github repsoitory and start the install.sh. If necessary change the ports and volume mounts in `docker-compose.yml`.  

`sudo git clone https://github.com/bibbox/app-taiga`

`sudo chmod +x install.sh`

`sudo ./install.sh`

The default port is 9000, you can start Taiga with

* `http://localhost:9000`


## Install within BIBBOX

Within BIBBOX you can use the [BIBBOX](https://bibbox.readthedocs.io/en/latest/ "BIBBOX") to install a lot of software tools. After the installation is finished you can start your application in the dashboard and follow these further [instructions](INSTALL-APP.md).


## Docker Images Used
* [taigaio/taiga-front](https://hub.docker.com/r/taigaio/taiga-front) 
* [taigaio/taiga-back](https://hub.docker.com/r/taigaio/taiga-back) 
* [taigaio/taiga-protected](https://hub.docker.com/r/taigaio/taiga-protected) 
* [taigaio/taiga-events](https://hub.docker.com/r/taigaio/taiga-events) 
* [rabbitmq](https://hub.docker.com/r/_/rabbitmq), offical container 
* [postgres](https://hub.docker.com/_/postgres), offical container
* [nginx](https://hub.docker.com/r/_/nginx), offical container 


### Documentation

* [Offical TIAGA Documentation](http://taigaio.github.io/taiga-doc/dist/)
* [TAIGA FAQ](http://taigaio.github.io/taiga-doc/dist/setup-faqs.html)
* [Upgrade Information (without docker)](http://taigaio.github.io/taiga-doc/dist/upgrades.html)

## Install Environment Variables

* SECRET_KEY
* ADMIN_USER
* ADMIN_EMAIL
* ADMIN_PASSWORD
* RABBITMQ_PASS
* POSTGRES_PASSWORD
* DEFAULT_FROM_EMAIL
* EMAIL_USE_TLS
* EMAIL_USE_SSL
* EMAIL_HOST
* EMAIL_PORT
* EMAIL_USER
* EMAIL_PASSWORD
* PUBLIC_REGISTER_ENABLED

## Mounted Volumes

* data/conf/proxy
* data/conf/back
* data/conf/front
* data/db
* data/media


