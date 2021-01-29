# Real-Estate-backend

Real estate app backend in django and rest-framework. Eclipse IDE with codemix plugin waas used ofr development.

Front end of the app "https://github.com/pshar33/Real-Estate-frontend/tree/master".

Eclipse IDE was used for development with Codemix plugin.

## Code requirements

* IDE that supports django/python project development(I used Eclipse IDE because it allows you to code both in React and python)
* pip
* pipenv
* django
* django-rest_framework
* django-cors-headers

## Setup
### Create an empty directory in your IDE Workspace,install git and then check the version of git by typing "git --version" in your directory.
### Clone my github repository to your local empty repository by typing "git clone -b master https://github.com/pshar33/Real-Estate-backend.git " 
Use pip to install pipenv

Run the following commands in cmd in your repository to install the necessary django:-
pipenv install django
pipenv install django-rest-framework
pipenv install django-cors-headers

Run the following commandst to create the necessary migrations and tables:-
python manage.py makemigrations
python manage.py migrate

And finally run the following command to start the django server:-
python manage.py runserver

Result can be viewed at http://localhost:8000/api




