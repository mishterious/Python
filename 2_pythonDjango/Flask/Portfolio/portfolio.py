from flask import Flask, render_template

DEBUG = True
PORT = 7000
HOST = "0.0.0.0"

app = Flask(__name__)


@app.route('/')
def portfolio():
    return render_template('/index.html')


@app.route('/projects')
def projects():
    return render_template('/projects.html')


@app.route('/about')
def about():
    return render_template('/about.html')


app.run(debug=DEBUG, port=PORT, host=HOST)