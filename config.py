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
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
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