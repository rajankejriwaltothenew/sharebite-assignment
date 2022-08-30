# About
This project is a Django Rest Framework backend for the assignment.

# Getting Started
## prerequisites
1. Python3
2. Virtualenv


## Setup process
1. Go to the project root directory
2. Create a virtualenv `virtualenv -p python env`
3. Activate the environment `source env/bin/activate`
4. Download all the requirements `pip install -r requirements.txt`
5. Migrate all the migrations `python manage.py migrate`


## start server
`python manage.py runserver`
should show the admin login page if it is running properly

rest of endpoints are here `http://127.0.0.1:8000/<endpoint>`

# Useful info
1. You can find all the api links and the payloads in api_list.txt file
2. To run the test cases `python manage.py test`