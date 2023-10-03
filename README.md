# taiga BIBBOX application

This container can be installed as [BIBBOX APP](https://bibbox.readthedocs.io/en/latest/ "BIBBOX App Store") or standalone. 

After the docker installation follow these [instructions](INSTALL-APP.md).

## Standalone Installation 

Clone the github repository. If necessary change the ports in the environment file `.env` and the volume mounts in `docker-compose.yml`.

```
git clone https://github.com/bibbox/app-taiga
cd app-taiga
docker network create bibbox-default-network
docker-compose up -d
```

The main App can be opened and set up at:
```
http://localhost:9000
```

## Install within BIBBOX

Visit the BIBBOX page and find the App by its name in the store. Click on the symbol and select install. Then fill the parameters below and name your App, click install again.

## Docker Images used
  - [postgres](https://hub.docker.com/r/postgres) 
  - [taigaio/taiga-back](https://hub.docker.com/r/taigaio/taiga-back) 
  - [taigaio/taiga-back](https://hub.docker.com/r/taigaio/taiga-back) 
  - [taigaio/taiga-back](https://hub.docker.com/r/taigaio/taiga-back) 
  - [rabbitmq](https://hub.docker.com/r/rabbitmq) 
  - [taigaio/taiga-front](https://hub.docker.com/r/taigaio/taiga-front) 
  - [taigaio/taiga-events](https://hub.docker.com/r/taigaio/taiga-events) 
  - [rabbitmq](https://hub.docker.com/r/rabbitmq) 
  - [taigaio/taiga-protected](https://hub.docker.com/r/taigaio/taiga-protected) 
  - [nginx](https://hub.docker.com/r/nginx) 


 
## Install Environment Variables
  - SECRET_KEY = Secret Phrase for the Taiga Backend,  please change for production
  - ADMIN_USER = Admin Username
  - ADMIN_EMAIL = Admin Email
  - ADMIN_PASSWORD = Admin Password
  - RABBITMQ_PASS = Rabbit Password,  please change for production
  - POSTGRES_PASSWORD = Postgres Password, please change for production
  - DEFAULT_FROM_EMAIL = Email
  - EMAIL_USE_TLS = True (default)
  - EMAIL_USE_TLS = False
  - EMAIL_USE_SSL = False (default)
  - EMAIL_USE_SSL = True
  - EMAIL_HOST = Email server
  - EMAIL_PORT = Port
  - EMAIL_USER = Username
  - EMAIL_PASSWORD = Password
  - PUBLIC_REGISTER_ENABLED = False (default)
  - PUBLIC_REGISTER_ENABLED = True
  - SECURE = http (default)
  - SECURE = https

  
The default values for the standalone installation are:
  - SECRET_KEY = changeforproduction
  - ADMIN_USER = admin
  - ADMIN_EMAIL = admin@bibbox.org
  - ADMIN_PASSWORD = changethispasswordinproductionenvironments
  - RABBITMQ_PASS = taiga
  - POSTGRES_PASSWORD = taiga
  - DEFAULT_FROM_EMAIL = no-reply@example.com
  - EMAIL_USE_TLS = "True"
  - EMAIL_USE_TLS = "False"
  - EMAIL_USE_SSL = "False"
  - EMAIL_USE_SSL = "True"
  - EMAIL_HOST = smtp.host.example.com
  - EMAIL_PORT = 587
  - EMAIL_USER = user
  - EMAIL_PASSWORD = changethispasswordinproductionenvironments
  - PUBLIC_REGISTER_ENABLED = "False"
  - PUBLIC_REGISTER_ENABLED = "True"
  - SECURE = :
  - SECURE = s:

  
## Mounted Volumes
### postgres Container
  - *./data/taiga-db-data:/var/lib/postgresql/data*
### taigaio/taiga-back Container
  - *./data/taiga-static-data:/taiga-back/static*
  - *./data/taiga-media-data:/taiga-back/media*
  - *./data/create_admin.py:/taiga-back/create_admin.py*
### taigaio/taiga-back Container
  - *./data/taiga-static-data:/taiga-back/static*
  - *./data/taiga-media-data:/taiga-back/media*
  - *./data/create_admin.py:/taiga-back/create_admin.py*
### taigaio/taiga-back Container
  - *./data/taiga-static-data:/taiga-back/static*
  - *./data/taiga-media-data:/taiga-back/media*
  - *./data/create_admin.py:/taiga-back/create_admin.py*
### rabbitmq Container
  - *./data/taiga-async-rabbitmq-data:/var/lib/rabbitmq*
### rabbitmq Container
  - *./data/taiga-events-rabbitmq-data:/var/lib/rabbitmq*
### nginx Container
  - *./data/taiga-gateway/nginx.conf:/etc/nginx/conf.d/default.conf*
  - *./data/taiga-gateway/proxy_params:/etc/nginx/proxy_params*
  - *./data/taiga-static-data:/taiga/static*
  - *./data/taiga-media-data:/taiga/media*

