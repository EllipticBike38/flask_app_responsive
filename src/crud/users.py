import datetime
from flask import Blueprint,request
import sqlite3
import uuid

class User():
    def create_user(values:list):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Users(Id, Name, Surname, Email, Password, Birthday) values ( ?, ?, ?, ?, ?, ?)", values)
            connection.commit()
        except sqlite3.IntegrityError:
            ...
        id_user=cursor.execute("select Id from Users where Email == ?", [values[3]]).fetchone()[0]
        connection.close()
        return {'user_id':id_user}

user=User()