from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login
from hashlib import md5


# tracks of user in user session
@login.user_loader
def load_user(id):
    '''[summary]
    
    Arguments:
        id {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    return User.query.get(int(id))



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    '''creates instances of users 
    
    Arguments:
        UserMixin {[type]} -- [description]
        db {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(255))
    # profile_pic_path = db.column(db.String())
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    # relationships
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    

    # python method to print class to the console
    def __repr__(self):
        return '<user {}>'.format(self.username)

    # generate password hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # verify password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # add gravatar
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)




class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'




# remember to add category property
class Post(db.Model):
    __tablename__ = 'post'
    '''creates instances of posts
    
    Arguments:
        db {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    content = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # relationships
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.relationship('Category', backref='type', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Subscribe():
    __tablename__ = 'subscribe'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    


class Category(db.Model):
    '''[summary]
    
    Arguments:
        db {[type]} -- [description]
    '''

    id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(20), index=True, unique=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))



class Comment(db.Model):
    __tablename__ = 'comment'

    '''[summary]
    
    Arguments:
        db {[type]} -- [description]
    '''
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)



class Quote:
    '''
    Quote class to create quotes
    '''

    def __init__(self,id, author, quote, permalink):
        self.id =id
        self.author = author
        self.quote = quote
        self.permalink = permalink
       





    