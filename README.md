# InnoWebsite
Innovision'16 Website

Built on Django 1.9.1

## Dependencies:

### 1. requests-oauthlib:

[Github](https://github.com/requests/requests-oauthlib)
#### Install:
    pip install requests requests_oauthlib

### 2. python-social-auth:

[Github](https://github.com/omab/python-social-auth)
[Docs](http://python-social-auth.readthedocs.org/en/latest/index.html)
#### Install:
    pip install python-social-auth


### 3. mysqlclient:

[Github](https://github.com/PyMySQL/mysqlclient-python)
#### Python and MySQL dev headers and libraries for mysqlclient:
    sudo apt-get install python-dev libmysqlclient-dev
#### Install:
    pip install mysqlclient

## Database: MySQL

Setup a databse with name **innovision**

    mysql> CREATE DATABASE innovision CHARACTER SET UTF8;

And a user **inno** with password **innovision**


    mysql> CREATE USER inno@localhost IDENTIFIED BY 'innovision';
    mysql> GRANT ALL PRIVILEGES ON innovision.* TO inno@localhost;
    mysql> FLUSH PRIVILEGES;