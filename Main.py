import flask
from flask import send_from_directory
from flask import abort, redirect, url_for

app = flask.Flask(__name__)

@app.route('/')
@app.route('/docs')

def index():
    return redirect("https://playversestudio.com/")

def docs():
    return "Hello, World!"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()