import os, json
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
    app.config['MYSQL_DB'] = 'IGH_users'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql = MySQL(app)


    #######################################
    #TODO: CREATE
    #######################################
    def insert_hashtags(username, hash_tags):
        cur = mysql.connection.cursor()
        cur.execute("SELECT hash_tags FROM user_info WHERE username='" + username +"'")
        fetched = cur.fetchone()
        fetched_list = json.loads(fetched['hash_tags'])
        updated_hashtags = fetched_list + hash_tags
        update_hashtags(username, updated_hashtags)
    
    def insert_insta_ids(username, insta_ids):
        cur = mysql.connection.cursor()
        cur.execute("SELECT insta_ids FROM user_info WHERE username='" + username +"'")
        fetched = cur.fetchone()
        fetched_list = json.loads(fetched['insta_ids'])
        updated_insta_ids = fetched_list + insta_ids
        update_insta_ids(username, updated_insta_ids)

    def insert_sources(username, sources):
        cur = mysql.connection.cursor()
        cur.execute("SELECT sources FROM user_info WHERE username='" + username +"'")
        fetched = cur.fetchone()
        fetched_list = json.loads(fetched['sources'])
        updated_sources = fetched_list + sources
        update_sources(username, updated_sources)

    #######################################
    #TODO: READ
    #######################################
    def get_user_data(username):
        '''Fetch all user data except login password'''
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user_info WHERE username='" + username +"'")
        user_data = cur.fetchone()
        user_data['hash_tags'] = json.loads(user_data['hash_tags'])
        user_data['insta_ids'] = json.loads(user_data['insta_ids'])
        return user_data


    #######################################
    # UPDATE
    #######################################
    def update_name(username, name):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_info SET name='" + name + "' WHERE username='" + username + "';")    
        mysql.connection.commit()

    def update_max_posts(username, max_posts):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_info SET max_posts='" + max_posts + "' WHERE username='" + username + "';")    
        mysql.connection.commit()

    def update_hashtags(username, hash_tags):
        cur = mysql.connection.cursor()
        # print(json.dumps(hash_tags))
        cur.execute("UPDATE user_info SET hash_tags='" + json.dumps(hash_tags) + "' WHERE username='" + username + "';")
        mysql.connection.commit()

    def update_insta_ids(username, insta_ids):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_info SET insta_ids='" + json.dumps(insta_ids) + "' WHERE username='" + username + "';")
        mysql.connection.commit()

    def update_sources(username, sources):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_info SET sources='" + sources + "' WHERE username='" + username + "';")
        mysql.connection.commit()

    def update_post_type(username, post_type):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_info SET post_type='" + post_type + "' WHERE username='" + username + "';")
        mysql.connection.commit()

    #######################################
    #TODO: DELETE
    #######################################


    #######################################
    # UPDATE
    #######################################

    @app.route('/dashboard')
    def index():
        username = request.args.get('username')
        user_data = get_user_data(username)
        # print(user_data)
        # insert_hashtags(username,['su','du'])
        return render_template('dashboard.html', user_data=user_data)

    @app.route('/edit_profile', methods=['POST'])
    def edit_profile():
        username = request.form.get('username')
        post_type = request.form.get('post_type')
        max_posts = request.form.get('max_posts')
        name = request.form.get('name')
        hashtags = request.form.get('hash_tags')
        insta_ids = request.form.get('insta_ids')
       
        hashtags_list = json.loads(hashtags.replace("'",'"'))
        insta_ids_list = json.loads(insta_ids.replace("'",'"'))

        update_name(username, name)
        update_max_posts(username, max_posts)
        update_hashtags(username, hashtags_list)
        update_insta_ids(username, insta_ids_list)
        update_post_type(username, post_type)
        
        return redirect(url_for('index', username=username))

    # simply return the app
    return app
