from flask import Flask, render_template, session, request, redirect, flash
import re

# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)

app.secret_key = "mish"
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'emailVal')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/checkemail', methods=['POST'])
def checkemail():
    if len(request.form['email_address']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        flash("The Email address you entered (___) is a VALID email address!")
        query = "INSERT into users(email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email':  request.form['email_address']
        }
        sentEmail = mysql.query_db(query, data)

        users = "SELECT * FROM users"
        allusers = mysql.query_db(users)
        print "________________________________________"
        print allusers
        return render_template('/success.html', allusers=allusers)


        # myemail = request.form['email_address']
        # # for x in user:
        # #     if x["email"] == myemail: 
        # #         print "yes"
        # #         return redirect('/')
        # #     else: 
        # #         print "no"
        # #         return redirect('/')
        # print myemail
        # return redirect('/')

app.run(debug=True)



