from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import  ValidationError, DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app import db
import sqlalchemy as sqla
from app.main.models import Tag

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post message', [Length(min=1, max=1500)])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])   
    tag = QuerySelectMultipleField('Tag', 
                                   query_factory= lambda : db.session.scalars(sqla.select(Tag)),
                                   get_label= lambda theTag : theTag.name,
                                   widget=ListWidget(prefix_label=False),
                                   option_widget=CheckboxInput())
    submit = SubmitField('Post')
    
class SortForm(FlaskForm):
    choice = SelectField('Sort By', choices=['Date', 'Title', '# of likes', 'Happiness level'])
    submit = SubmitField('Refresh')