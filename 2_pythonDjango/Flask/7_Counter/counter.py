from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000


@app.route('/')
def index():
    session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])



app.run(debug=DEBUG, host=HOST, port=PORT)