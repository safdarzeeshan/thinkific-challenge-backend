# Thinkific Code Challenge API

url - http://thinkificapi.zeeshansafdar.com/api

This project creates an API to allow a user to

Register
method - POST
url - /registration/

curl -X POST -H 'Content-Type: application/json' -d '{"email": "test@test.com","password1": "test1234","password2": "test1234"}' http://thinkificapi.zeeshansafdar.com/api/registration/


Login
method - POST
url - /login

curl -X POST -H 'Content-Type: application/json' -d '{"email": "test@test.com","password": "test1234"}' http://thinkificapi.zeeshansafdar.com/api/login/

Get user's current integer
method - GET
url - /current_int

curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Token XXXXX' -d '{"email": "test@test.com","password": "test1234"}' http://thinkificapi.zeeshansafdar.com/api/current_int/

Get user's next integer /next_integer
method - GET
url - /next_integer

Set user's current integer /curent_integer
method - PUT
url - /current_int

## Build & development

To install dependencies `pip install -r requirements.txt`

In `thinkific_api/settings.py` change your database settings

To create the database `./manage.py migrate`

To run locally `./manage.py runserver`

