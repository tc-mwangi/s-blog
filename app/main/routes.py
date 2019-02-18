from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from werkzeug.urls import url_parse
from app.models import User, Post, Quote
from app.main.forms import EditProfileForm, PostForm, EditPostForm
from app.main import bp
from ..requests import get_quotes


# A decorator provides mapping between a url and a function.
# you can chain more than one url to the same fuction.
@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''
    form=PostForm()
    if form.validate_on_submit():

        post = Post(body=form.post.data, author=current_user)
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))

    

    
    
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    # get quotes
    random_quotes = get_quotes()

    quote= random_quotes['quote']
    author= random_quotes['author']
    


    # quotes = [
    # {
    #     'author': 'Rich Cook',
    #     'quote': 'Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.', 
        
    # },
    # {
        
    #     'author': 'Robert Sewell',
    #     'quote': 'If Java had true garbage collection, most programs would delete themselves upon execution.', 
        
    # }
    # ]
    return render_template('index.html', title='Home Page', form=form, posts=posts, quote=quote, author=author)




@bp.route('/user/<username>')
@login_required
def user(username):
    '''[summary]
    
    Arguments:
        username {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
   

    user = User.query.filter_by(username=username).first_or_404()

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@bp.route('/post_pitch', methods=['GET', 'POST'])
@login_required
def post_pitch():
    form = PostForm(current_user.username)
    
   
    return render_template('post_pitch.html', title='Post Pitch',
                           form=form)


@bp.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    form=PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your blog is now live!')
        return redirect(url_for('main.index'))

    # elif request.method == 'GET':
    #     form.username.data = current_user.username
    #     form.about_me.data = current_user.about_me
    return render_template('create_blog.html', title='Create a Blog',
                           form=form)


@bp.route('/blog_article', methods=['GET', 'POST'])
@login_required
def blog_article():

    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    
    return render_template('blog_article.html', title='Blog Article'
                           )


@bp.route('/edit_blog', methods=['GET', 'POST'])
@login_required
def edit_blog():
    form=PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your blog has been updated!')
        return redirect(url_for('main.index'))

    # elif request.method == 'GET':
    #     form.username.data = current_user.username
    #     form.about_me.data = current_user.about_me
    return render_template('edit_blog.html', title='Create a Blog',
                           form=form)


@bp.route('/my_blog_list')
@login_required
def my_blog_list():
    '''[summary]
    
    Arguments:
        username {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''
   

    # user = User.query.filter_by(username=username).first_or_404()
    # posts = Post.query.filter_by(author_id=author_id).all()

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('my_blog_list.html', user=user, posts=posts)











    