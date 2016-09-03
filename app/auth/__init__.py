from flask import (current_app,
                   Blueprint,
                   render_template,
                   flash,
                   session,
                   redirect,
                   url_for,
                   request,
                   g)
from flask_login import LoginManager
auth = Blueprint('auth',
                 __name__,
                 url_prefix='/auth',
                 template_folder='/templates')

lm = LoginManager()

from . import views
