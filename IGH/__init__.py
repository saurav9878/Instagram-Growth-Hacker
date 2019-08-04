import os
from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

def create_app(test_config=None):
    # create app and configure the app
    app = Flask(__name__, instance_relative_config=True)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'test'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql = MySQL(app)


    #######################################
    # CREATE
    #######################################


    #######################################
    # READ
    #######################################
    def get_user_data(username):
        cur = mysql.connection.cursor()
        # Assuming the table name is USERS
        # Put Non-lists data in USERS
        cur.execute("SELECT * FROM USERS WHERE USERNAME='" + username +"'")
        user_data = cur.fetchone()
        return user_data

    def get_insta_ids(username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT insta_ids FROM INSTA_IDS WHERE USERNAME='" + username +"'")
        user_data = cur.fetchall()
        insta_ids = []
        for i in range(len(user_data)):
            insta_ids.append(user_data[i]['insta_ids'])
        return insta_ids


    def get_hashtags(username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT hash_tags FROM HASHTAGS WHERE USERNAME='" + username +"'")
        user_data = cur.fetchall()
        hash_tags = []
        for i in range(len(user_data)):
            hash_tags.append(user_data[i]['hash_tags'])
        return hash_tags


    #######################################
    # UPDATE
    #######################################
    def update_name(username,name):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE USERS SET name='" + name + "' WHERE username='" + username + "';")    
        mysql.connection.commit()

    def update_max_posts(username, max_posts):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE USERS SET max_posts='" + max_posts + "' WHERE username='" + username + "';")    
        mysql.connection.commit()


    #######################################
    # DELETE
    #######################################



    #######################################
    # UPDATE
    #######################################

    @app.route('/dashboard')
    def index():
        username = request.args.get('username')
        user_data = get_user_data(username)
        user_data['insta_ids'] = get_insta_ids(username)
        user_data['hash_tags'] = get_hashtags(username)
        print(user_data)
        return render_template('dashboard.html', user_data=user_data)

    @app.route('/edit_profile', methods=['POST'])
    def edit_profile():
        username = request.form.get('username')
        max_posts = request.form.get('max_posts')
        print(username)
        name = request.form.get('name')
        # hashtags = request.form.get('hashtags')
        # insta_ids = request.form.get('insta_ids')
        update_name(username, name)
        update_max_posts(username, max_posts)
        # update_hashtags(username, hashtags)
        # update_insta_ids(username, insta_ids)
        return redirect(url_for('index', username=username)), 200

    # simply return the app
    return app
