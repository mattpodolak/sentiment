from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

class InputForm(FlaskForm):
    search_input = StringField('Enter Search Query', validators=[DataRequired()])
    submit = SubmitField('Process Data')