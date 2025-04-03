# Ипортируем библиотеки.
import os
import json
import random
import smtplib
#from data.user import User
#from write_data import add_user, add_job
from flask import Flask, url_for, request, session, render_template, redirect
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user

from data import db_session
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.addeventform import AddEventForm
from data.Usersdb import User
from data.event import Event


app = Flask(__name__)
app.config['SECRET_KEY'] = "roblox"
db_session.global_init("db/blogs.db")

login_manager = LoginManager()
login_manager.init_app(app)
#login_manager.login_view = 'login'


# это нужно для авторизации
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

# отправка сообщений
@app.route("/sent_email/<adress>")
def sent_email(adress):
    code = random.randint(10000, 99999)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('calendar12341@gmail.com', 'qweras123a')
    smtpObj.sendmail("calendar12341@gmail.com", adress, code)
    smtpObj.quit()
    return render_template('main.html', title='Подтверждение почты')

# страница главная
@app.route("/")
def main():
    db_sess = db_session.create_session()
    userr = db_sess.query(User).filter(User.is_active == True).first()
    return render_template('news.html', title='Главное', user=userr)


# страница Профиля
@app.route("/personal_account")
def personal_account():
    db_sess = db_session.create_session()
    userr = db_sess.query(User).filter(User.is_active == True).first()
    return render_template('profile.html', title='Профиль', user=userr)


# страница Активности
@app.route("/active")
def active():
    db_sess = db_session.create_session()
    userr = db_sess.query(User).filter(User.is_active == True).first()
    event = db_sess.query(Event).all()
    return render_template('active.html', title='Активности', user=userr, event=event)

# страница добовление активность
@app.route('/addeventform', methods=['GET', 'POST'])
def addeventform():
    form = AddEventForm()
    db_sess = db_session.create_session()
    userr = db_sess.query(User).filter(User.is_active == True).first()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        event = Event(
            name=form.name.data,
            description=form.description.data,
            organizers=form.organizers.data,
            email=form.email.data,
            data=form.data.data,
            time=form.time.data,
            genres=form.genres.data
        )
        db_sess.add(event)
        db_sess.commit()
        return redirect("/personal_account")
    return render_template('eventform.html', title='Авторизация', form=form, user=userr)

# страница Авторизации
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user:# and user.check_password(form.password.data):
            user.is_active = True
            db_sess.commit()
            login_user(user, remember=form.remember_me.data)
            return redirect("/active")
        return render_template('login.html',
                                title='Авторизация',
                                form=form,
                                message="Неправильный логин или пароль")
    return render_template('login.html', title='Авторизация', form=form)

# страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        #if form.password.data != form.password_again.data:
        # return render_template('register.html', title='Регистрация',
        # form=form,
        # message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            login=form.login.data,
            password=form.password.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            role=form.role.data,
            is_active=False
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# Страница для выхода\
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    db_sess = db_session.create_session()
    userr = db_sess.query(User).filter(User.is_active == True).first()
    userr.is_active = False
    db_sess.commit()
    return redirect('/')


# Запускаем сервер.
if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1", debug=True)


