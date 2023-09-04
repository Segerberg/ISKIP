from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('E-post', validators=[DataRequired()])
    password1 = PasswordField('Lösenord', validators=[DataRequired()])
    password2 = PasswordField('Bekräfta lösenord', validators=[DataRequired(), EqualTo('password1')])
    consent = BooleanField('Samtyck', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('E-post', validators=[DataRequired()])
    password = PasswordField('Lösenord', validators=[DataRequired()])

class AddSurveyForm(FlaskForm):
    name = StringField('Namn', validators=[DataRequired()])
    type = StringField('Branch', validators=[DataRequired()])


class SurveyForm(FlaskForm):
    q1a = RadioField('a)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1b = RadioField('b)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1c = RadioField('c)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1d = RadioField('d)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1e = RadioField('e)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1f = RadioField('f)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1g = RadioField('g)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1h = RadioField('h)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1i = RadioField('i)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1j = RadioField('j)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1k = RadioField('k)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2a = RadioField('a)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2b = RadioField('b)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2c = RadioField('c)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2d = RadioField('d)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2e = RadioField('e)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2f = RadioField('f)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2g = RadioField('g)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2h = RadioField('h)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2i = RadioField('i)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2j = RadioField('j)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2k = RadioField('k)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2l = RadioField('l)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2m = RadioField('m)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2n = RadioField('n)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2o = RadioField('o)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2p = RadioField('p)', validators=[DataRequired()], choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q3a = RadioField('a)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3b = RadioField('b)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3c = RadioField('c)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3d = RadioField('d)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3e = RadioField('e)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3f = RadioField('f)', validators=[DataRequired()], choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q4a = SelectField('Hur definerar du dig?', validators=[DataRequired()],
                      choices=[("", "Välj"), (1, "Man"), (2, 'Kvinna'), (3, 'Icke-binär'), (4, "Vill ej ange")])

    q4b = SelectField('Jag har arbetat för min nuvarande arbetsgivare i...',
                      choices=[("", "Välj antal år"), (1, "1 år"), (2, '2år')])
    q4b = SelectField('Jag har arbetat i min nuvarande arbetsgrupp i...',
                      choices=[("", "Välj antal år"), (1, "1 år"), (2, '2år')])
    q4c = SelectField('Jag har arbetat för min nuvarande chef i...',
                      choices=[("", "Välj antal år"), (1, "1 år"), (2, '2år')])
    q4d = SelectField('Jag har arbetat med liknande arbetsuppgifter i...',
                      choices=[("", "Välj antal år"), (1, "1 år"), (2, '2år')])
    q4e = SelectField('Har du en arbetsledande funktion?',
                      choices=[("", "Välj"), (1, "Ja"), (2, 'Nej')])
