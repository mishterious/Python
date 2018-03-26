from flask import Flask, render_template, request, redirect

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print name
    return redirect('/')


app.run(debug=DEBUG, host=HOST, port=PORT)
