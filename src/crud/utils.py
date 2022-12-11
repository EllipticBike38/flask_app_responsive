import datetime
from flask import Blueprint,request
import sqlite3
import uuid

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