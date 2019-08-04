import os
from flask import Flask, request, render_template
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
    mysql = MySQL(app)

    def get_name(username):
        cur = mysql.connection.cursor()
        # Assuming the table name is USERS
        cur.execute("SELECT NAME FROM USERS WHERE USERNAME = '"+ username +"'")
        name = cur.fetchone()
        return name[0]


    @app.route('/dashboard')
    def index():
        username = request.args.get('username')
        print('username')
        name = get_name(username)
        # name = get_name(username)
        return render_template('dashboard.html', name=name)

    @app.route('/add_user_param')
    def add_param():
        username = request.form.get('username')
        

    # simply return the app
    return app
