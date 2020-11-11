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

The environment variables are as follows:

DB_ENGINE corresponds to the database variable ENGINE in the `settings.py` file.
DB_HOST corresponds to the database variable HOST in the `settings.py` file.
DB_PORT corresponds to the database variable PORT in the `settings.py` file.
DB_NAME corresponds to the database variable NAME in the `settings.py` file.
DB_PASSWORD corresponds to the database variable PASSWORD in the `settings.py` file.
KEY corresponds to the database variable SECRET_KEY in the `settings.py` file.

### Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
