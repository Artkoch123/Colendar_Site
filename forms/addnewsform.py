from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, IntegerField, StringField, BooleanField, SubmitField, TimeField
from wtforms.validators import DataRequired


class AddEventForm(FlaskForm):
    name = EmailField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    data = StringField('Дата', validators=[DataRequired()])
    submit = SubmitField('Опубликовать новость')