from flask import Flask, render_template, session, request, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'fullFriends')


@app.route('/') 
def index(): 
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template("index.html", friends=friends)


@app.route('/reachTheTop', methods=["POST"])
def newFriends():
    addNew = request.form['addName']
    addAge = request.form['addAge']

    query = "INSERT INTO friends(name, age, created_at, updated_at) VALUES (:addNew, :addAge, NOW(), NOW())"
    data = { 
        'addNew' : request.form['addName'],
        'addAge' : request.form['addAge']
    }
    friends = mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)