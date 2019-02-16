# # import os
# # from dotenv import load_dotenv

# # basedir = os.path.abspath(os.path.dirname(__file__))
# # load_dotenv(os.path.join(basedir, '.env'))


# # class Config(object):
# #     SECRET_KEY = os.environ.get('secretbunny') or 'beachbunny'
# #     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
# #         'sqlite:///' + os.path.join(basedir, 'app.db')
# #     SQLALCHEMY_TRACK_MODIFICATIONS = False
# #     LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
# #     MAIL_SERVER =os.environ.get('MAIL_SERVER')
# #     MAIL_PORT =int(os.environ.get('MAIL_PORT') or 25)
# #     # TLS- transport layer security to enable encryption
# #     MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') is not None
# #     MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
# #     MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
# #     ADMINS = ['saber.dangermouse@gmail.com']



# import os

# class Config:

    
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     UPLOADED_PHOTOS_DEST ='app/static/images'

#     #  email configurations
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     SUBJECT_PREFIX = 'PitchView'
#     SENDER_EMAIL = 'saber.dangermouse@gmail.com'

# # simple mde  configurations
#     # SIMPLEMDE_JS_IIFE = True
#     # SIMPLEMDE_USE_CDN = True
#     # @staticmethod
#     # def init_app(app):
#     #     pass


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
#     pass

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/pitch_test'

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/pitch'
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig

# }


import os


class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '32193281319283129832'
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'mwangiloisexx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/images'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_MAROON_URL")
    pass


class DevConfig(Config):
    """
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/pitch'
    DEBUG = True


class TestConfig(Config):
    """
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://saberdanger:cartoonroyalty@localhost/pitch-test'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}