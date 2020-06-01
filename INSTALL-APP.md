## BIBBOX TAIGA APP Installation 

## Login

* user: admin
* password: 123123

Please change the password. 

## Add new users

## Configration

### Email 
### LDAP

## Backup instructions

* set the env APPID, subdomain of the installed app

        export APPID=taiga

* Backup the database App directory, replace APPID with the id (subdomain) of the installed app. 

        /opt/bibbox/application-instance/${APPID}-app-taiga
        
* Backup the whole data directory 
    
        /opt/bibbox/application-instance/${APPID}-app-taiga/data
        
* Backup the posgres database with the command
       
        docker exec  -t ${APPID}-taiga-db pg_dumpall -c -U postgres > ${APPID}-backup_`date +%d-%m-%Y"_"%H_%M_%S`.sql

   if you forgot the database root password, you can lookup it in the docker-compose file. 
   
        grep POSTGRES /opt/bibbox/application-instance/${APPID}-app-taiga/docker-compose.yml

## After the installation

Have a nice ride with the new Admins youngtimer.

![FINAL](install-screen-final.jpg)
