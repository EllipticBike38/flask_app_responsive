import datetime
from hashlib import sha256
from flask import Blueprint,request
import sqlite3
import uuid
import crud
blueprint = Blueprint('user', __name__)


@blueprint.route('/login', methods=["POST"])
def user_login():
    form=request.form
    pwd=crud.user.find_password_by_email(form['email'])
    password=sha256(form['password'].encode('utf8')).hexdigest()
    if password==pwd:
        print('ok')
    else:
        print('Nope')
    return form
    

@blueprint.route('/signup', methods=["POST"])
def user_signup():
    form=request.form
    data=[
        str(uuid.uuid4()), #id
        form['name'],
        form['surname'],
        form['email'],
        sha256(form['password'].encode('utf8')).hexdigest(),
        int(datetime.datetime.fromisoformat(form['birthdate']).timestamp())
    ]
    return crud.user.create_user(data)
   