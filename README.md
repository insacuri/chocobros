# chocobros

This'll be the code for the chocobros fftcg site

Written in python as a learning exercise but might one day become something more.

## Running locally

Heres a basic guide on how to set this up locally
 - Running in a vitualenv is recommended `python3 -m venv chocobros`
 - `pip3 install -r requirements.txt`
 - `export FLASK_APP=chocobros.py`
 - `flask run`

You can also run it in docker by doing:
 - `docker build -t chocobros .`
 - `docker run -p 5000:80 chocobros` (Should be running at localhost:5000)

 Also requires mongodb to be running at localhost:27017 (will be configurable later on)


 # TODO

 Stuff to do in the future
  - decide on DB technology (mongodb?)
  - authentication (experiment with bcrypt or something similar? 2FA with a time based token?)
  - Deck builder
  - Splitting out non-visible functionality into an API?
