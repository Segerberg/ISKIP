#!/usr/bin/env python
import datetime
import json
import os
import uuid

from flask import render_template, session, request, send_file, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import SurveyForm, RegistrationForm, LoginForm, AddSurveyForm, ActivateSurveyForm
from app.models import User, Survey, Response
from flask_login import current_user, login_user, logout_user, login_required
from app.utils import send_mail_confirmation, calc_dim, mean, create_pdf
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename


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
                        active=False)
        db.session.add(survey)
        db.session.commit()
        flash('Enkät skapad', 'alert-success')
        return redirect(request.url)

    return render_template('surveys.html', surveys=surveys, AddSurveyForm=add_survey_form)

@app.route('/surveys/<id>')
@login_required
def survey_detail(id):
    min_responses = int(os.getenv('MIN_RESPONSES',5))
    activate_survey_form = ActivateSurveyForm()
    survey = db.session.query(Survey).filter(Survey.user_id == current_user.id).filter(Survey.id == id)\
        .join(Response, Response.survey_id==id).first()
    if not survey:
        survey = db.session.query(Survey).filter(Survey.user_id == current_user.id).filter(Survey.id == id).first()

    return render_template('survey_detail.html', survey=survey, activate_survey_form=activate_survey_form, min_responses=min_responses)

@app.route('/toggle-survey/<id>', methods=['GET','POST'])
@login_required
def toggle_survey_status(id):
    survey = db.session.query(Survey).filter(Survey.user_id == current_user.id).filter(Survey.id == id).first()
    if survey.active:
        survey.active = False
        db.session.commit()
    else:
        survey.active = True
        db.session.commit()
    return redirect(url_for('survey_detail',id=id))



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
    survey = db.session.query(Survey).filter(Survey.id==survey_id).first()
    if survey and survey.active:
        form = SurveyForm()
        return render_template('respond.html', form=form, survey_id=survey_id)
    return render_template('survey_error.html', survey=survey)


@app.route('/respond_post/<survey_id>', methods=['POST'])
def respond_post(survey_id):
    form = SurveyForm()
    # if form.validate_on_submit(): # todo
    survey = db.session.query(Survey).filter(Survey.id == survey_id).first()
    if survey:
        data = Response(survey_id=survey_id, created=datetime.datetime.utcnow(), data=form.data)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('thankyou'))
    return "403"  # todo better response

@app.route('/thankyou/', methods=['GET'])
def thankyou():
    return render_template('thankyou.html')



@app.route('/report/<survey_id>', methods=['GET'])
def report(survey_id):
    survey = db.session.query(Survey).filter(Survey.user_id == current_user.id).filter(Survey.id == survey_id)\
        .join(Response, Response.survey_id==survey_id).first()

    LP_calc_vals = (4.4955,	0.9928)
    LI_calc_vals = (3.6558,	1.0021)
    LR_calc_vals = (4.5322,	0.8862)
    GE_calc_vals = (4.2341,	0.8786)
    GL_calc_vals = (4.1484,	0.8658)
    GR_calc_vals = (4.4804,	0.9194)
    GH_calc_vals = (4.0300,	1.0427)

    LP_lst = []
    LI_lst = []
    LR_lst = []
    GE_lst = []
    GL_lst = []
    GR_lst = []
    GH_lst = []


    for resp in survey.responses:
        LP = [resp.data['q1a'],resp.data['q1b'],resp.data['q1c'],resp.data['q1d']]
        LP_lst.append(mean(LP))

        LI = [resp.data['q1e'], resp.data['q1f'], resp.data['q1g']]
        LI_lst.append(mean(LI))

        LR = [resp.data['q1h'], resp.data['q1i'], resp.data['q1j'], resp.data['q1k']]
        LR_lst.append(mean(LR))

        GE =  [resp.data['q2a'],resp.data['q2b'],resp.data['q2c'],resp.data['q2d']]
        GE_lst.append(mean(GE))

        GL =  [resp.data['q2e'],resp.data['q2f'],resp.data['q2g'],resp.data['q2h']]
        GL_lst.append(mean(GL))

        GR =  [resp.data['q2i'],resp.data['q2j'],resp.data['q2k'],resp.data['q2l']]
        GR_lst.append(mean(GR))

        GH =  [resp.data['q2m'],resp.data['q2n'],resp.data['q2o'],resp.data['q2p']]
        GH_lst.append(mean(GH))



    L_Prioritet = calc_dim(mean(LP_lst),LP_calc_vals[0],LP_calc_vals[1])
    L_Involvering = calc_dim(mean(LI_lst),LI_calc_vals[0],LI_calc_vals[1])
    L_Rattvisa = calc_dim(mean(LR_lst), LR_calc_vals[0], LR_calc_vals[1])

    G_Engagemang = calc_dim(mean(GE_lst), GE_calc_vals[0], GE_calc_vals[1])
    G_Larande = calc_dim(mean(GL_lst), GL_calc_vals[0], GL_calc_vals[1])
    G_Regel = calc_dim(mean(GR_lst), GR_calc_vals[0], GR_calc_vals[1])
    G_Hotbild = calc_dim(mean(GH_lst), GH_calc_vals[0], GH_calc_vals[1])

    data = {
        "respondents": survey.responses.count(),
        "group_name":survey.name,
        "L_Prioritet":L_Prioritet,
        "L_Involvering":L_Involvering,
        "L_Rattvisa":L_Rattvisa,
        "G_Engagemang":G_Engagemang,
        "G_Larande":G_Larande,
        "G_Regel":G_Regel,
        "G_Hotbild":G_Hotbild
    }
    pdf_bytes = create_pdf(data)
    safe_filename = secure_filename(f'ISKIP resultat från enkätundersökning_{survey.name}')
    return send_file(
        pdf_bytes,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'{safe_filename}.pdf'
    )