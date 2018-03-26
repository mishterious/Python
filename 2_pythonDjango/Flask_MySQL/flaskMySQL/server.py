
from flask import Flask, render_template, session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query

print mysql.query_db("SELECT * FROM users")

@app.route('/') 
def index(): 
    return render_template("index.html")
    

app.run(debug=True)