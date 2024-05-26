from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField,FileSize
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User
from flaskblog import app

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_field(self,field):
    #     if True:
    #         raise ValidationError('validation Message')

    def validate_username(self,username):
        with app.app_context():
            user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username is taken. Please choose a different one')
    def validate_email(self,email):
        with app.app_context():
            user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    picture=FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    # def validate_field(self,field):
    #     if True:
    #         raise ValidationError('validation Message')

    def validate_username(self,username):
        if username.data!=current_user.username:
            with app.app_context():
                user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That Username is taken. Please choose a different one')
    def validate_email(self,email):
        if email.data!=current_user.email:
            with app.app_context():
                user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one')



class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit=SubmitField('Post')
