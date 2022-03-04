## BIBBOX TAIGA APP Installation 

## Login 

### Standalone

* user: admin
* password: vendetta

Please change the password. 

### BIBBOX

* Set during installation

## Add new users

Once a new user is added to a project a email notifictaion is automatically send to the provided email address.

* Create a project -> settings -> members -> +NEW MEMBER

### If Email is disabled.

Add the user to the project in the same way:
* Create a project -> settings -> members -> +NEW MEMBER

No Email will/can be send. You can check the Postgres database for the invitation `token` of that member in the table projects_memberships (Using adminer or a similar app).
Once you have the `token` you can share the invitatio link with the new member:
* [TAIGA_URL]/invitation/`token`
* e.g. http://taiga.silicolabv4.bibbox.org/invitation/1a2b3c4d-5e6f-7g8h-9i8j-7k6l5m4n3o2p

## Configration

### Email 

#### Standalone

* Default disabled. Can be changed in the docker-compose.yml file: Uncomment following lines and configure your SMTP server
  *  EMAIL_BACKEND: "django.core.mail.backends.smtp.EmailBackend"
  *  DEFAULT_FROM_EMAIL: "no-reply@example.com"
  *  EMAIL_USE_TLS: "False"
  *  EMAIL_USE_SSL: "False"
  *  EMAIL_HOST: "smtp.host.example.com"
  *  EMAIL_PORT: 587
  *  EMAIL_HOST_USER: "user"
  *  EMAIL_HOST_PASSWORD: "password"

#### BIBBOX

* Set during installation


## After the installation

Have a nice ride with the new Admins youngtimer.

![FINAL](assets/install-screen-final.jpg)
