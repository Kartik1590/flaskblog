from flask import Flask,render_template,url_for,redirect,flash
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__) #__name__ is the name of the module  if we run this script than __name__=__main__
app.config['SECRET_KEY']='e048910b9c64801eb7d9a1cd60bfb806'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'


db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login' # same thing that we pass in url_for method
login_manager.login_message_category='info' # bootstrap info class
login_manager.login_message="Please login here"
from flaskblog import routes
