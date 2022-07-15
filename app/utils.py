from flask_mail import Message, Mail
from flask import render_template
import os


def send_mail_confirmation(user):
    mail = Mail()
    token = user.get_mail_confirm_token()
    msg = Message(
        os.environ.get('MAIL_SUBJECT') or "Please Confirm Your Email",
        recipients=[user.email],
    )
    msg.html = render_template("mail_confirm.html", token=token, baseurl=os.environ.get('BASEURL'))
    mail.send(msg)
