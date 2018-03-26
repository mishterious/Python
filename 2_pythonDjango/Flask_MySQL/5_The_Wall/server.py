from flask import Flask, render_template, redirect, request, flash, session
import re
import md5
import os, binascii
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)

app.secret_key = "hieuwjoisjergiuhjeo"
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    # query = 'SELECT * FROM comments LEFT JOIN posts ON comments.posts_post_id = posts.post_id'
    # print mysql.query_db(query)
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
                flash("Welcome back {}!".format(allusers[0]['first_name']))
                session['user'] = allusers
                # this means we have a successful login!
                return redirect('/thewall')

            else:
                flash("Invalid PASSWORD!!!!")
                redirect('/')
        else:
            flash("Invalid Email Address!")
            redirect('/')
        
        for all in allusers: 
            if all['email'] == request.form['email']:
                # print all['email']
                # print request.form['email']
                return redirect('/')
            else:

                return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    print "WERE HERE !!!!!! ---------------------"
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash("You're names cannot be blank!")
        return redirect('/newreg')
    # elif and str.isalpha(request.form['first_name']) is Falsy:
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/newreg')
    elif request.form['password'] != request.form['confirm_password'] and request.form['password'] < 8: 
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


@app.route('/newreg')
def newreg():
    return render_template('register.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    # allusers = session['user']
    # # were storing 

    query = "INSERT into posts(post, created_at, updated_at, users_user_id) VALUES (:post, NOW(), NOW(), :users_user_id)"
    data = {
        'post': request.form['newpost'],
        'users_user_id': session['user'][0]['user_id']
    }
    addposts = mysql.query_db(query, data)


    return redirect('/thewall')


@app.route('/thewall')
def thewall():
    getPosts = "SELECT posts.post, posts.created_at, users.first_name, users.last_name, users.user_id FROM posts JOIN users ON posts.users_user_id = users.user_id ORDER BY posts.created_at DESC"
    allPosts = mysql.query_db(getPosts)
    return render_template('thewall.html', allPosts=allPosts)


@app.route('/newcomment', methods=['POST'])
def newcomment():
    print request.form['user_id']
    #  you can see the user_id here but, it's also stored in sessino, and you want to store it in the person who is making the comment on another post.
    comment = "INSERT into comments(mycomment, created_at, updated_at, users_user_id, posts_post_id) VALUES (:comment, NOW(), NOW(), :users_user_id, :posts_post_id)"
    data = {
        'comment': request.form['newComment'],
        'users_user_id': session['user'][0]['user_id'],
        'posts_post_id': request.form['user_id']
    }
    allComments = mysql.query_db(comment, data)
    return redirect('/wallcomment')


@app.route('/wallcomment')
def wallcomment():

    getPosts = "SELECT posts.post_id, posts.post, posts.created_at, users.first_name, users.last_name, users.user_id FROM posts JOIN users ON posts.users_user_id = users.user_id ORDER BY posts.created_at DESC"
    allPosts = mysql.query_db(getPosts)
    # Get all of the posts in order of last(top) to the first(bottom)

    getComments = "SELECT comments.comment_id, comments.mycomment, comments.created_at, users.first_name, users.last_name, comments.users_user_id, comments.posts_post_id FROM comments JOIN posts ON comments.posts_post_id = posts.post_id JOIN users ON posts.users_user_id = users.user_id ORDER BY posts.created_at ASC;"
    # Get all of the comment in order of first(top) to the last(bottom)
    
    allComments = mysql.query_db(getComments)

    return render_template('wallcomments.html', allPosts=allPosts, allComments=allComments)


@app.route('/remove', methods=['POST'])
def remove():
    deletecomment = "DELETE FROM comments WHERE comments.comment_id = :id"
    data = {
        'id': request.form['deleteComment']
    }
    removeComment = mysql.query_db(deletecomment, data)
    print removeComment
    return redirect('/wallcomment')


app.run(debug=True)
