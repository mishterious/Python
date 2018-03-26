from flask import Flask, render_template

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    # if "counter" not in session:
    #     session['counter'] = 0 
    # else: 
    #     session['counter'] += 1
    return render_template('index.html')


@app.route('/ninjas')
def ninjas():

    return render_template("ninjas.html")


@app.route('/dojos/new')
def dojos():

    return render_template("dojos.html")


app.run(debug=DEBUG, host=HOST, port=PORT)
