from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, IntegerField, StringField, BooleanField, SubmitField, TimeField
from wtforms.validators import DataRequired


class AddEventForm(FlaskForm):
    name = EmailField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    organizers = StringField('Организаторы', validators=[DataRequired()])
    data = StringField('Дата', validators=[DataRequired()])
    time = StringField('Время', validators=[DataRequired()])
    genres = StringField('Жанры', validators=[DataRequired()])
    submit = SubmitField('Опубликовать событие')