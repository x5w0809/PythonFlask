from flask import Flask
from flask_wtf import Form,FlaskForm
from wtforms import StringField,SubmitField,validators,PasswordField,SelectField
from wtforms.fields.html5 import EmailField
from model import UserRegister
from wtforms import BooleanField
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

class FormRegister(Form):
    username = StringField('username',validators=[validators.DataRequired(),validators.Length(1,20)])
    email = EmailField('email',validators=[validators.DataRequired(),validators.Length(1,50),validators.Email()])
    password = PasswordField('password',validators=[validators.DataRequired(),validators.Length(6,20),validators.EqualTo('password2',message='password need match')])
    password2 = PasswordField('confirm your password',validators=[validators.DataRequired()])
    city = SelectField('City',choices=[(1,'桃園'),(2,'台北'),(3,'新竹'),(4,'基隆')],coerce=int)
    submit = SubmitField('Register')


    def validate_email(self,field):
        if UserRegister.query.filter_by(email=field.data).first():
            raise ValueError('Email already register by somebody')
    def validate_username(self,field):
        if UserRegister.query.filter_by(username=field.data).first():
            raise ValueError('Email already register by somebody')

class FormLogin(FlaskForm):
    email = EmailField('Email',validators=[validators.DataRequired(),validators.Length(1,20),validators.email()])
    password = PasswordField('Password',validators=[validators.DataRequired(),validators.Length(6,20)])
    remember_me = BooleanField('Keep logged in!')
    submit = SubmitField('login')

