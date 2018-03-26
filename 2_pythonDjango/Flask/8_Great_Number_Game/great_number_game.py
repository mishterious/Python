from flask import Flask, render_template, request, redirect, url_for, session

import random 
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=["POST"])
def check():
    print "Hellooooo yea we are here!!!"
    guess = request.form['guess']
    print guess
    return redirect('/')


app.run(debug=DEBUG,host=HOST, port=PORT)