from flask import Flask, render_template

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


app.run(debug=DEBUG, host=HOST, port=PORT)
