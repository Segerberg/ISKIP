from flask_mail import Message, Mail
from flask import render_template
import os
import pdfkit
from jinja2 import Environment, FileSystemLoader
import plotly.graph_objects as go
from plotly.io import to_image
import base64
from io import BytesIO



def send_mail_confirmation(user):
    mail = Mail()
    token = user.get_mail_confirm_token()
    msg = Message(
        os.environ.get('MAIL_SUBJECT') or "Please Confirm Your Email",
        recipients=[user.email],
    )
    msg.html = render_template("mail_confirm.html", token=token, baseurl=os.environ.get('BASEURL'))
    mail.send(msg)

def mean(lst):
    lst = [int(x) for x in lst if x]
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        pass

def calc_dim(val, normmean, stddev):
    """

    :param val: Medelvärde data
    :param normmean: Medelvärde Normdata
    :param stddev: Standardavvikelse Normdata
    :return:
    """
    result = 30 * ((val - normmean) / stddev) + 100
    return result


def create_chart(name,L_Prioritet,L_Involvering,L_Rattvisa,G_Engagemang,G_Larande,G_Regel,G_Hotbild):
    fig_data = [
        go.Scatterpolar(
            fill='none',
            name=name,
            r=[L_Prioritet, L_Involvering, L_Rattvisa, G_Engagemang, G_Larande, G_Regel, G_Hotbild],
            theta=['L_Prioritet', 'L_Involvering', 'L_Rättvisa', 'G_Engagemang', 'G_Lärande', 'G_Regel-legitimitet',
                   'G_Hotbild'],
            type='scatterpolar'
        ),
        go.Scatterpolar(
            fill='none',
            name='Riksurval',
            r=[100, 100, 100, 100, 100, 100, 100],
            theta=['L_Prioritet', 'L_Involvering', 'L_Rättvisa', 'G_Engagemang', 'G_Lärande', 'G_Regel-legitimitet',
                   'G_Hotbild'],
            type='scatterpolar'
        )
    ]
    # Layout settings
    fig_layout = go.Layout(
        showlegend=True,
        polar=dict(
            radialaxis=dict(angle=90, visible=True, showline=False, range=[50, 150])
        )
    )
    fig = go.Figure(data=fig_data, layout=fig_layout)
    width = 600
    height = 400
    image_bytes = to_image(fig, format='png',width=width, height=height, scale=2, engine='kaleido')
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    return image_base64


def create_pdf(data):
    file_loader = FileSystemLoader('./app')
    env = Environment(loader=file_loader)
    template = env.get_template('templates/report.html')
    b64 = create_chart(data['group_name'],data['L_Prioritet'], data['L_Involvering'],data['L_Rattvisa'],data['G_Engagemang'], data['G_Larande'], data['G_Regel'], data['G_Hotbild'])

    output = template.render(data=data, b64=b64)
    opts = {'javascript-delay': 1000,
            'no-stop-slow-scripts': None,
            'debug-javascript': None,
            "enable-local-file-access": ""}
    pdf_bytes = pdfkit.from_string(output, False, options=opts)

    return BytesIO(pdf_bytes)



