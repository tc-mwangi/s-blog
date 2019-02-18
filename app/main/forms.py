from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User, Post


class EditProfileForm(FlaskForm):
    '''[summary]
    
    Arguments:
        FlaskForm {[type]} -- [description]
    '''

    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[
        DataRequired(), Length(min=1, max=800)])   
    post = SubmitField('Post')


class PostPitchForm(FlaskForm):
    ''' '''
    category = StringField('Category', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[Length(min=0, max=400)])
    submit = SubmitField('Post')





