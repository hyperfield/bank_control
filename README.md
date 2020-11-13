## Bank Remote Alarm Control

### Description

Bank Remote Alarm Control is a Web application for monitoring activity in the bank safe.

### How to install

If Python 3 is not yet installed then download it from [python.org](http://www.python.org) for your operating system and install. Then use `pip` (or `pip3` if you also have Python 2 on your system) to install the dependencies:

`pip install -r requirements.txt`

### How to launch

`python manage.py runserver 0.0.0.0:8000`

Then go to [http://127.0.0.1:8080](http://127.0.0.1:8080) in your Web browser.

### Environment variables

The environment variables are defined as per the correspondence list for `settings.py` below:

DB_ENGINE <->  ENGINE  
DB_HOST <-> HOST  
DB_PORT <-> PORT  
DB_NAME <-> NAME  
DB_USERNAME <-> USERNAME  
DB_PASSWORD <-> PASSWORD  
KEY <-> SECRET_KEY  

### Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
