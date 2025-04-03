from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, IntegerField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторить пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    role = StringField('Роль', validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    submit = SubmitField('Войти')