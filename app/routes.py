#!/usr/bin/env python
import functools
from flask import render_template, session, request, copy_current_request_context, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import SurveyForm, RegistrationForm, LoginForm
from app.models import User, Survey
from flask_login import current_user, login_user, logout_user, login_required
from app.utils import send_mail_confirmation
import os
import sys
from sqlalchemy.exc import IntegrityError


@app.route('/')
def index():
    login_form = LoginForm()
    return render_template('index.html', LoginForm=login_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.confirmed :
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                next = request.args.get("next")
                return redirect(next or url_for('surveys'))
        flash("Inloggning misslyckad",  "alert-danger")
    return render_template('index.html', LoginForm=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Utloggad", "alert-success")
    return redirect(url_for('index'))


@app.route('/survey')
@login_required
def survey():
    form = SurveyForm()
    return render_template('survey.html', form=form)

@app.route('/surveys')
@login_required
def surveys():
    return render_template('surveys.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(email=form.email.data)
            user.set_password(form.password1.data)
            db.session.add(user)
            send_mail_confirmation(user)
        except IntegrityError:
            db.session.rollback()
            flash('Användare finns redan', 'alert-danger')
        db.session.commit()
    return render_template("register.html", form=form)


@app.route("/confirm_email/<token>")
def confirm_email(token):
    email = User.verify_mail_confirm_token(token)
    print(email)
    if email:

        user = db.session.query(User).filter(User.email == email).one_or_none()
        user.confirmed = True
        db.session.commit()
        return redirect(url_for("index"))

    else:
        flash('token invalid', 'alert-danger')
        return render_template("token_invalid.html")


@app.route('/survey_post', methods=['post'])
def survey_post():
    form = SurveyForm()
    print(form.data)
    return redirect(url_for('survey'))  # todo redirect to "Thank you"

