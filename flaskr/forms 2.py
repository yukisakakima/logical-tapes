from click import password_option
from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User

#ログイン画面で利用
class LoginForm(Form):
    email = StringField('Mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

#登録画面で利用
class RegisterForm(Form):
    email = StringField('Mail:', validators=[DataRequired(), Email()])
    username = StringField('Name:', validators=[DataRequired()])
    password = PasswordField(
        'Password:', validate=[DataRequired(), EqualTo('password_confirm', message='Incorrect password.')]
        )
    password_confirm = PasswordField('Confirm password:', validators=[DataRequired()])
    submit = SubmitField('Register') 
    
def validate_email(self, field):
    if User.select_by_email(field.data):
        raise ValidationError('This email address has already been registered.')

