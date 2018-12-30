from flask import render_template, flash, redirect, url_for,request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Review
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
        return render_template('index.html',title='Home')



@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if user is already logged-in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    #login-process
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login failed. Try again.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')                        #this is here to redirect the user to the page he wanted to visit
        if not next_page or url_parse(next_page).netloc!='':        # blocks redirection to sides from other domains
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a member!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
