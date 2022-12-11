import datetime
from flask import Blueprint,request
import sqlite3
import uuid
import crud
blueprint = Blueprint('user', __name__)


@blueprint.route('/login', methods=["POST"])
def user_login():
    form=request.form
    return form
    

@blueprint.route('/signup', methods=["POST"])
def user_signup():
    form=request.form
    data=[
        str(uuid.uuid4()), #id
        form['name'],
        form['surname'],
        form['email'],
        form['password'],
        int(datetime.datetime.fromisoformat(form['birthdate']).timestamp())
    ]
    return crud.user.create_user(data)
   