from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User, Post, Comment


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


class SubscribeForm(FlaskForm):
    ''' '''
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Subscribe')




class EditPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[
        DataRequired(), Length(min=1, max=1000)])   
    post = SubmitField('Update')



class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[DataRequired()])
    submit = SubmitField('Submit')





