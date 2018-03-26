from flask import Flask, render_template, request, redirect

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['POST'])
def survey():

    name = request.form['name']
    city = request.form['city']
    language = request.form['language']
    optional_Comment = request.form['optional_Comment']

    print name 
    print city
    print language
    print optional_Comment

    return render_template('result.html', name=name, city=city, language=language,  optional_Comment=optional_Comment)


app.run(debug=DEBUG, host=HOST, port=PORT) 