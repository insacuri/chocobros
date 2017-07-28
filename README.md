# chocobros

This'll be the code for the chocobros fftcg site

Written in python as a learning exercise but might one day become something more.

## Running locally

Heres a basic guide on how to set this up locally
 - Running in a vitualenv is recommended `python3 -m venv chocobros`
 - `pip3 install Flask`
 - `export FLASK_APP=chocobros.py`
 - `flask run`

 # TODO

 Stuff to do in the future
  - Set up docker container
  - decide on DB technology (mongodb?)
  - authentication (experiment with bcrypt or something similar? 2FA with a time based token?)
  - Deck builder
  - Splitting out non-visible functionality into an API?
