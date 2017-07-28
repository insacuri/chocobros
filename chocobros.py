from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['card_name'] :
            return redirect(url_for('search') + '/' + request.form['card_name'])
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/search')
@app.route('/search/<card_name>')
def search(card_name=None):
    return render_template('search.html', card_name=card_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
