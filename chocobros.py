from flask import Flask, request, g, redirect, url_for, abort, \
     render_template, flash
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(__name__)

#TODO: Get this config from somewhere else
app.config.update(dict(
    DATABASE_URL='localhost',
    DATABASE_PORT=27017
))

def connect_client():
    """Connects to the specific database."""
    return MongoClient(app.config['DATABASE_URL'], app.config['DATABASE_PORT'])

def get_client():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'mongodb'):
        g.mongodb = connect_client()
    return g.mongodb

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['card_name'] :
            return redirect(url_for('search') + '/' + request.form['card_name'])
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
@app.route('/search/<card_name>')
def search(card_name=None):

    client= get_client()
    db = client.chocobros

    result = db.cards.find({"name": card_name})
    return render_template('search.html', card_name=card_name, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
