from .users import blueprint as bp_users


from flask import Blueprint

api = Blueprint('apis', __name__,
                        template_folder='templates',
                        static_folder='static')

#TODO https://github.com/pallets/flask/issues/4865
#! I problemi di eredità del subdomain sono un problema che ancora esiste, 
#! si apettano aggiornamenti di Flask.           
api.register_blueprint(bp_users,
                        url_prefix="/user", subdomain="api" )
