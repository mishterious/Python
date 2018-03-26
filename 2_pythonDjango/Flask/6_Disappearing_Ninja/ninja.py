from flask import Flask, render_template, request, redirect, url_for

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/ninja', methods=['GET'])
def ninja():

    return render_template('allNinjas.html')


@app.route('/<color>')
def eachpic(color):
    print color
    if color == "blue":
        print color
        return render_template('blue.html')

    elif color == "red":
        print color
        return render_template('red.html')

    elif color == "orange":
        return render_template('orange.html')

    elif color == "purple":
        return render_template('purple.html')
    
    else: 
        return render_template('non_ninja.html')


app.run(debug=DEBUG, host=HOST, port=PORT)