from flask import Flask, render_template

add = Flask(__name__)

@app('/')


def hello_world():
    return render_template('index.html')
app.run(debug=True)
