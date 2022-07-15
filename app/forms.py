from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('E-post', validators=[DataRequired()])
    password1 = PasswordField('Lösenord', validators = [DataRequired()])
    password2 = PasswordField('Bekräfta lösenord', validators = [DataRequired(),EqualTo('password1')])
    consent = BooleanField('Samtyck', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('E-post', validators=[DataRequired()])
    password = PasswordField('Lösenord', validators = [DataRequired()])


class SurveyForm(FlaskForm):
    q1a = RadioField('a)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2,'Stämmer mycket dåligt'),
                                                                 (3,'Stämmer ganska dåligt'), (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'), (6, 'Stämmer fullständigt')])

    q1b = RadioField('b)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2,'Stämmer mycket dåligt'),
                                                                 (3,'Stämmer ganska dåligt'), (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'), (6, 'Stämmer fullständigt')])


