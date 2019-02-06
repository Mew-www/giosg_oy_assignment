### Required background software (installed and running)  
* **NGINX + Gunicorn** *(described further below)* 
    * or **Apache2 + mod_wsgi**
        * *[Linux guide](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/)* 
        * *[Windows guide, except link Django's wsgi.py instead of described wsgi_app.py](https://beamtic.com/installing-mod-wsgi-apache-windows)*
* **Redis-server** [[Linux/Debian](https://redislabs.com/ebook/appendix-a/a-1-installation-on-debian-or-ubuntu-linux/)] [[Mac/OSX](https://redislabs.com/ebook/appendix-a/a-2-installing-on-os-x/)] [[Win32/Win64](https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/)]  

### Clone this repo and set-up virtualenv
`git clone <repository url>`  
`cd <repository name>`  
`virtualenv venv --python=python3`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  

### Set-up environment variables and init database models
Environment variables to declare (on the user running WSGI):  
* GI_ASSIGNMENT_SECRET_KEY='an-instance-specific-new-secret-key'  
    Use the following snippet to generate a new key:  
    `from django.core.management.utils import get_random_secret_key`  
    `get_random_secret_key()`
      
* GI_ASSIGNMENT_ALLOWED_HOSTS='comma,separated,list,of,domains'  
    Optional, defaults to "localhost". If you're hosting/accessing locally from "127.0.0.1" you may have to change this to that. Or any other domain(s) being used.

* GI_ASSIGNMENT_DEBUG='0'  
    Optional, defaults to False. Only value "1" sets it on.

Migrate database models:  
`cd gi_assignment`  
`python manage.py migrate`