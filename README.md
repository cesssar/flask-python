API Flask rodando no Apache

Habilitar mod_rewrite no Apache

$ cd /etc/apache2/mods-available
a2enmod rewrite

Em minha máquina (Ubuntu - Vivid Vervet) o local é este aqui…

/etc/apache2/apache2.conf
De qualquer forma você deve procurar o trecho abaixo.

<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride None # <---- ATENÇÂO
        Require all granted
</Directory>
E alterar conforme abaixo.

<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride All # <---- ATENÇÂO
        Require all granted
</Directory>
Agora basta reiniciar o Apache.

/etc/init.d/apache2 restart


Introduction
Apache HTTP Server (usually just called Apache) is fast and secure and runs over half of all web servers around the globe.
Apache is a free software and is distributed by the Apache Software Foundation, which promotes various free and open-source advanced web technologies.

mod_wsgi is an Apache HTTP Server module by Graham Dumpleton that provides a WSGI compliant interface for hosting Python based web applications under Apache.
N.B: We would be using python3.6 for development so we should install mod_wsgi (py3)

Flask is a popular Python web framework, meaning it is a third-party Python library used for developing web applications.

Continue reading further, to learn integration of all 3 of them to achieve perks of Apache on your flask web app...

Requirements
apache2
mod_wsgi (for python3)
flask
Installation Guide
Install Apache
sudo apt update
sudo apt install apache2

Install mod_wsgi
for python 3.6 (preferable)
sudo apt-get install libapache2-mod-wsgi-py3 python-dev

for python 2.7

sudo apt-get install libapache2-mod-wsgi-py python-dev

Install flask
(Assuming you have pip3.6 installed)
pip3.6 install flask

Check browser if it's running Apache
apache2 -f /etc/apache2/apache2.conf -k start

apache_localhost.png

Let's Create our flask application
Let create a nested directory named as ExampleFlask in home direcory (location could be anything)

mkdir -p ~/ExampleFlask/ExampleFlask

Add below 3 files in the inner ExampleFlask directory

__init__.py
Empty file

my_flask_app.py

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello world!"
if __name__ == "__main__":
    app.run()
my_flask_app.wsgi
The name of above wsgi file should be same as the flask application
Add a shebang line to specify which interpreter to use
#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/username/ExampleFlask/')
from my_flask_app import app as application
application.secret_key = 'anything you wish'

Let's create the config file for our flask application
vim /etc/apache2/sites-available/ExampleFlask.conf

 
<VirtualHost *:80>
     # Add machine's IP address (use ifconfig command)
     ServerName 192.168.1.103
     # Give an alias to to start your website url with
     WSGIScriptAlias /testFlask /home/username/ExampleFlask/my_flask_app.wsgi
     <Directory /home/username/ExampleFlask/ExampleFlask/>
     		# set permissions as per apache2.conf file
            Options FollowSymLinks
            AllowOverride None
            Require all granted
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     LogLevel warn
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
Enable the file with a2ensite:

sudo a2ensite /etc/apache2/sites-available/ExampleFlask.conf

Restart apache2
So, the new changes could take effect.

apache2 -f /etc/apache2/apache2.conf -k stop
apache2 -f /etc/apache2/apache2.conf -k start

Check browser if it's running Apache at your machine IP address, provided in config
apache_default.png

Check browser if it's running your flask app at your machine IP address with prefix /testFlask
url : http://192.168.1.103/testFlask/

apache_flask_app_running.png

Congratulations, we have successfully deployed a flask application on ubuntu 18.04

==================================================================================

No crontab -e adicionar uma tarefa para limpeza da pasta

40 10 * * * rm -f /var/www/html/audios
