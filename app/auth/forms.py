from wtforms import (StringField,
                     PasswordField,
                     BooleanField)
from wtforms.validators import (DataRequired,
                                equal_to,email)
from flask_wtf import Form


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(),
                                                         equal_to('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=False)

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(message='Must provide a password. ;-)')])
    remember_me = BooleanField('Remember me', default=False)

