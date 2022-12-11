from flask import Flask, render_template
from flaskwebgui import FlaskUI
from api import db_init, api

app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = "mini-desktop-pc.homenet.telecomitalia.it:5555"
app.register_blueprint(api, subdomain="api")


context={'menus':[
        ('Home','#'),
        ('Contacts','#'),
        ('Settings','#'),
        ('About Us','#'),
        ('Login','login')
    ]}
@app.route('/')
def index():
    return render_template('index.html',**context)


@app.route('/login')
def login():
    return render_template('login.html',**context)

@app.route('/signup')
def signup():
    return render_template('signup.html',**context)

if __name__ == "__main__":
    # FlaskUI(app=app, server="flask",width=500, height=500).run()
    db_init()
    app.run("0.0.0.0",5555,True)

    