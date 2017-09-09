from flask import Flask, request, g, redirect, url_for, abort, \
     render_template, flash
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(__name__)
#TODO configure a logger
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

def substitute_tokens_for_html(result):
    """Subsitutes [var] tokens for HTML.  This saves having to have HTML in the database (which should
    only contain data).
    """
    #TODO use array to store variable names and loop over that.
    result['text'] = result['text'].replace('[wind]', "<img src='/static/icons/wind.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[ice]', "<img src='/static/icons/ice.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[water]', "<img src='/static/icons/water.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[fire]', "<img src='/static/icons/fire.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[earth]', "<img src='/static/icons/earth.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[lightning]', "<img src='/static/icons/lightning.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[light]', "<img src='/static/icons/light.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[dark]', "<img src='/static/icons/dark.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[s]', "<img src='/static/icons/special.png' class='small-icon'/>")
    result['text'] = result['text'].replace('[dull]', "<img src='/static/icons/dull.png' class='small-icon'/>")
    return result


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    #TODO field valiation
    if not request.args.get('name'):
        return render_template('search.html', results=[])
    client= get_client()
    db = client.chocobros

    # Doing case insensitivity here is inefficient, but over a few hundred results it's fine.
    results = db.cards.find({"name":{"$regex":request.args.get('name', ''), "$options": "-i"}})
    #TODO pagination of results over a certain amount
    transformed_results = []
    for result in results:
        result = substitute_tokens_for_html(result)
        transformed_results.append(result)
    return render_template('search.html', results=transformed_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
