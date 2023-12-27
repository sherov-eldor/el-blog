from wtforms import form, fields, validators
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    login = fields.StringField(validators=[validators.InputRequired()])
    password = fields.PasswordField(validators=[validators.InputRequired()])
    submit = fields.SubmitField('Submit')