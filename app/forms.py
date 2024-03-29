from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('E-post')
    password1 = PasswordField('Lösenord')
    password2 = PasswordField('Bekräfta lösenord', validators=[DataRequired(), EqualTo('password1')])
    consent = BooleanField('Samtyck')


class LoginForm(FlaskForm):
    email = StringField('E-post')
    password = PasswordField('Lösenord')


class AddSurveyForm(FlaskForm):
    name = StringField('Namn')
    type = RadioField('Näringsgren',choices=[(1, "Jordbruk, skogsbruk och fiske"),
(2, "Fastighetsverksamhet (handel, förmedling uthyrning och förvaltning av fastigheter"),
(3,"Utvinning av kol, petroleum, gas, metall och mineral"),
(4,"Verksamhet och konsulttjänster inom juridik, ekonomi, vetenskap och teknik"),
(5,"Tillverkningsindustri, tillverkning av varor och produkter"),
(6,"Uthyrning av maskiner fordon, personal, bevakning, resebyrå-, kontorstjänster och andra stödtjänster till företag"),
(7,"Försörjning av el, gas, värme och kyla"),
(8,"Offentlig förvaltning (stat, region, kommun) inklusive socialförsäkring"),
(9,"Vatten & avlopp, avfallshantering"),
(10,"Försvar, polis, rättsväsende, kriminalvård"),
(11,"Bygg- och anläggningsverksamhet"),
(12,"Utbildning (förskola, grundskola, gymnasium, eftergymnasial, högskola)"),
(13,"Handel (inkluderar även försäljning och reparation av motorfordon)"),
(14,"Hälso- och sjukvård, omsorg och sociala tjänster"),
(15,"Transporter (väg, järnväg, sjö och flyg) och magasinering"),
(16,"Kultur, nöje och fritid"),
(17,"Hotell- och restaurangverksamhet"),
(18,"Förvärvsarbete i hushåll och serviceverksamhet till hushåll"),
(19,"IT-, informations- och kommunikationsverksamhet"),
(20,"Internationella organisationer, ambassader"),
(21,"Finans- och försäkringsverksamhet"),
(22,"Annan typ av verksamhet")])
    no_participants = IntegerField('Antal deltagare')


class ActivateSurveyForm(FlaskForm):
    active = BooleanField('active')

class SurveyForm(FlaskForm):
    q1a = RadioField('a)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q1b = RadioField('b)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q1c = RadioField('c)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1d = RadioField('d)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1e = RadioField('e)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1f = RadioField('f)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1g = RadioField('g)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q1h = RadioField('h)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q1i = RadioField('i)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1j = RadioField('j)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q1k = RadioField('k)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q2a = RadioField('a)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2b = RadioField('b)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])

    q2c = RadioField('c)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])

    q2d = RadioField('d)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2e = RadioField('e)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2f = RadioField('f)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2g = RadioField('g)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2h = RadioField('h)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2i = RadioField('i)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2j = RadioField('j)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2k = RadioField('k)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2l = RadioField('l)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2m = RadioField('m)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2n = RadioField('n)', choices=[(1, "Stämmer inte alls"), (2, 'Stämmer mycket dåligt'),
                                                                 (3, 'Stämmer ganska dåligt'),
                                                                 (4, 'Stämmer ganska bra'),
                                                                 (5, 'Stämmer mycket bra'),
                                                                 (6, 'Stämmer fullständigt')])
    q2o = RadioField('o)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q2p = RadioField('p)', choices=[(6, "Stämmer inte alls"), (5, 'Stämmer mycket dåligt'),
                                                                 (4, 'Stämmer ganska dåligt'),
                                                                 (3, 'Stämmer ganska bra'),
                                                                 (2, 'Stämmer mycket bra'),
                                                                 (1, 'Stämmer fullständigt')])
    q3a = RadioField('a)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3b = RadioField('b)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3c = RadioField('c)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3d = RadioField('d)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3e = RadioField('e)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q3f = RadioField('f)', choices=[(1, "Aldrig"), (2, 'Nästan aldrig'),
                                                                 (3, 'Sällan'),
                                                                 (4, 'Ibland'),
                                                                 (5, 'Ofta'),
                                                                 (6, 'Nästan alltid'),
                                                                 (7, 'Alltid')])
    q4a = SelectField('Hur definerar du dig?',
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
