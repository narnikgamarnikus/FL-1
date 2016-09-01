from flask import Flask, request, render_template, flash, redirect, url_for, session, g, session
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import mapper,sessionmaker
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, unicode
from config import basedir
from wtforms import StringField,PasswordField,BooleanField,validators
from wtforms.validators import DataRequired, equal_to, Email
from flask_wtf.csrf import CsrfProtect,validate_csrf,generate_csrf
from werkzeug import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
CsrfProtect(app)
from app import views, models, forms