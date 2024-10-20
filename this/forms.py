from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # name = StringField('Name')
    submit = SubmitField('Submit')