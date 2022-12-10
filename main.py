from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)



@app.route('/')
def index():
    context={'menus':[
        'Home',
        'Contacts',
        'Settings',
        'About Us',
        'Login'
    ]}
    return render_template('index.html',**context)

if __name__ == "__main__":
    # FlaskUI(app=app, server="flask",width=500, height=500).run()
    app.run("0.0.0.0",5555,True)

    