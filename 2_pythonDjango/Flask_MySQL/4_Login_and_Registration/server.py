from flask import Flask, render_template, redirect, request, session
import re
import md5
import os, binascii
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)

app.secret_key = "hieuwjoisjergiuhjeo"
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'loginReg')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/checkpass', methods=['POST'])
def checkpass():
    print "================================"
    if len(request.form['password']) < 8:
        flash("Password cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        user_query = "SELECT * FROM users WHERE users.email = :email"
        newUser = {
            'email': request.form['email']
        }
        allusers = mysql.query_db(user_query, newUser)
        
        if len(allusers) != 0:
            salt = allusers[0]['salt']
            encrypted_password = md5.new(request.form['password'] + salt).hexdigest()
            if allusers[0]['password'] == encrypted_password:
                flash("The Email address you entered (___) is a VALID email address!")
                # this means we have a successful login!
            else:
                flash("Invalid PASSWORD!!!!")
        else:
            flash("Invalid Email Address!")

        # password = md5.new(request.form'password']).hexdigest() == allusers.users.password
        print "almost there!!"
        print request.form['password']
        print allusers
        print "===================="
        
        for all in allusers: 
            if all['email'] == request.form['email']:
                print all['email']
                print request.form['email']
                return redirect('/')
            else:
                return redirect('/')


@app.route('/newreg')
def newreg():
    return render_template('registration.html')


@app.route('/register', methods=['POST'])
def register():
    print "WERE HERE !!!!!! ---------------------"
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash("You're names cannot be blank!")
        return redirect('/newreg')
    # elif and str.isalpha(request.form['first_name']) is Falsy:
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/newreg')
    if request.form['password'] != request.form['confirm_password'] and request.form['password'] < 8: 
        flash("Your passwords don't match and needs more that 8 letters. Please try again!")
        return redirect('/newreg')
    else:
        flash("Hey you've logged in!!")
        salt = binascii.b2a_hex(os.urandom(15))
        password = md5.new(request.form['password'] + salt).hexdigest()
        query = "INSERT into users(first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email':  request.form['email'],
            'password': password,
            'salt': salt
        }
        addUser = mysql.query_db(query, data)
        print addUser
        return redirect('/')


app.run(debug=True)
