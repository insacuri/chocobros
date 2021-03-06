# chocobros
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/183634e5dafe47deab5b131a258379c0)](https://www.codacy.com/app/insacuri/chocobros?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=insacuri/chocobros&amp;utm_campaign=Badge_Grade)

This'll be the code for the chocobros fftcg site

Written in python as a learning exercise but might one day become something more.

## Running locally

Heres a basic guide on how to set this up locally
 - Ensure mongodb is running at localhost:27017
 - Running in a vitualenv is recommended `python3 -m venv chocobros` (`~/chocobros/bin/activate` if you've already done this step before)
 - `pip3 install -r requirements.txt`
 - `export FLASK_APP=chocobros.py`
 - `flask run`

You can also run it in docker by doing:
 - `docker build -t chocobros .`
 - `docker run -p 5000:80 chocobros` (Should be running at localhost:5000)

 # TODO

 Stuff to do in the future
  - Advanced Search functionality (Power, Type, etc)
  - Configuration management (mongodb, etc)
  - Login and Authentication (experiment with bcrypt or something similar? 2FA using TOTP?)
  - Deck builder
  - Splitting out non-visible functionality into an API?
  - Blog/deck of the week section
