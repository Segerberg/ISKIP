#!/usr/bin/env python
import datetime
import uuid

from flask import render_template, session, request, copy_current_request_context, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import SurveyForm, RegistrationForm, LoginForm, AddSurveyForm, ActivateSurveyForm
from app.models import User, Survey, Response
from flask_login import current_user, login_user, logout_user, login_required
from app.utils import send_mail_confirmation
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


@app.route('/surveys', methods=["GET", "POST"])
@login_required
def surveys():
    surveys = db.session.query(Survey).filter(Survey.user_id == current_user.id).all()
    add_survey_form = AddSurveyForm()
    if add_survey_form.validate_on_submit():
        survey = Survey(name=add_survey_form.name.data,
                        type=add_survey_form.type.data,
                        created=datetime.datetime.utcnow(),
                        user_id=current_user.id,
                        survey_id=str(uuid.uuid4()),
                        active=False)
        db.session.add(survey)
        db.session.commit()
        flash('Enkät skapad', 'alert-success')
        return redirect(request.url)

    return render_template('surveys.html', surveys=surveys, AddSurveyForm=add_survey_form)

@app.route('/surveys/<id>')
@login_required
def survey_detail(id):
    activate_survey_form = ActivateSurveyForm()
    survey = db.session.query(Survey).filter(Survey.user_id == current_user.id).filter(Survey.survey_id == id)\
        .join(Response, Response.survey_id==1).first()

    return render_template('survey_detail.html', survey=survey, activate_survey_form=activate_survey_form)



@app.route('/register', methods=["GET", "POST"])
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
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Användare finns redan', 'alert-danger')

    return render_template("register.html", form=form)


@app.route("/confirm_email/<token>")
def confirm_email(token):
    email = User.verify_mail_confirm_token(token)

    if email:
        user = db.session.query(User).filter(User.email == email).one_or_none()
        user.confirmed = True
        db.session.commit()
        flash('Din konto är nu aktiverat', 'alert-success')
        return redirect(url_for("index"))

    else:
        flash('token invalid', 'alert-danger')
        return render_template("token_invalid.html")

@app.route('/respond/<survey_id>', methods=['GET'])
def respond(survey_id):
    form = SurveyForm()
    return render_template('respond.html', form=form, survey_id=survey_id)

@app.route('/respond_post/<survey_id>', methods=['POST'])
def respond_post(survey_id):
    form = SurveyForm()
    # if form.validate_on_submit(): # todo
    data = Response(survey_id=survey_id, created=datetime.datetime.utcnow(), data=form.data)
    db.session.add(data)
    db.session.commit()
    return redirect(url_for('thankyou'))


@app.route('/thankyou/', methods=['GET'])
def thankyou():
    return render_template('thankyou.html')

@app.route('/report', methods=['GET'])
def report():
    data = {
        "respondents": 23,
        "group_name":"Förebildsförvaltningen"
    }
    return render_template('report.html', data=data)