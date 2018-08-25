from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

class InputForm(FlaskForm):
    twitter = StringField('Enter Twitter Account', validators=[DataRequired()])
    submit = SubmitField('Process Data')