from flask import Flask
#from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from .auth import auth
from .auth.models import db
from .auth import lm
from flask_bootstrap import Bootstrap

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    #lm = LoginManager(app)
    lm.init_app(app)
    db.init_app(app)
    Bootstrap(app)
    lm.login_view = 'login'
    app.register_blueprint(auth)
    CsrfProtect(app)
    return app
