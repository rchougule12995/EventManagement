Event Management web application which allows users to create new events, edit or delete
active events, search events.

The main objective of this web application is to share events between a closed group of users.

The following operations are performed in the web application:
a. Create new events
b. Edit or delete active events.
c. Archive old events
d. Search for events.
e. Share an event with user.

Requirements:
1. Python 3.6 and above
2. Virtual Environment (pipenv or virtualenv)

Run the below commands when downloaded and extracted the Event Management folder:
*************************************************
cd event_management

pip install virtualenv
virtualenv newenv

pip install -r requirements.txt

cd src

python manage.py runserver
*************************************************
Running Migrations:
Not required, as the web application will have sample data in the DB.

#python manage.py migrate
