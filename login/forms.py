from wtforms import Form, StringField,PasswordField, BooleanField
from wtforms import validators, SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Email()])
    submit = SubmitField('Login')