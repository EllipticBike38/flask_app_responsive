import datetime
from flask import Blueprint,request
import sqlite3
import uuid

api = Blueprint('apis', __name__,
                        template_folder='templates',
                        static_folder='static')

@api.route('/user/login', methods=["POST"])
def user_login():
    form=request.form
    return form
    

@api.route('/user/signup', methods=["POST"])
def user_signup():
    form=request.form
    data=[
        str(uuid.uuid4()), #id
        form['name'],
        form['surname'],
        form['email'],
        form['password'],
        int(datetime.datetime.fromisoformat(form['date']))
    ]
    create_user(data)
        
    
def create_user(values:list):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("insert into Users(Id, Name, Surname, Email, Password, Birthday) values ( ?, ?, ?, ?, ?, ?)", values)

    connection.commit()
    connection.close()


def db_init():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                (Id TEXT, 
                Name TEXT not null,
                Surname TEXT not null, 
                Email TEXT unique not null, 
                Password TEXT not null, 
                Birthday INT not null,
                Primary key(Id)
                )''')

    connection.commit()
    connection.close()