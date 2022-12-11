import datetime
from flask import Blueprint,request
import sqlite3
import uuid

class User():
    def create_user(self, values:list):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Users(Id, Name, Surname, Email, Password, Birthday) values ( ?, ?, ?, ?, ?, ?)", values)
            connection.commit()
        except sqlite3.IntegrityError:
            ...
        connection.close()
        id_user = self.find_user_by_email(values[3])
        return {'user_id':id_user}
    
    def find_id_by_email(self, email:str):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            id_user=cursor.execute("select Id from Users where Email == ?", 
                                [email]).fetchone()[0]
        except TypeError:
            id_user = ''
        finally:
            connection.close()  
        return id_user 

    def find_user_by_email_or_id(self, email:str=None, id:str=None):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            user=cursor.execute("select Id, Name, Surname, Email, Birthday from Users where Email == ? or Id == ?", 
                                [email,id]).fetchone()
        except TypeError:
            user = []
        finally:
            connection.close()  
        return user 
    def find_password_by_email(self, email:str):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            pwd=cursor.execute("select Password from Users where Email == ?", 
                                [email]).fetchone()[0]
        except TypeError:
            pwd = ''
        finally:
            connection.close()  
        return pwd 
        

user=User()