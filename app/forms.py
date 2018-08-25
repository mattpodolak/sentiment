from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

class InputForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign In')