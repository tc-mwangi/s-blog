import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_bootstrap import Bootstrap
from config import config_options


# initialize extensions/scope: global/create instance of extension class
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = ('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()

#*change config class to config name
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
   
    #register blueprints/are inactive until initialized.
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # configure UploadSet
    # configure_uploads(app, photos)

    

    return app


from app import models
