import os
import tempfile

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'I7QkQImQ6468QJkKQJ434QHJHFLSssjd' # variable ENV
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['alexandre.pape@epitech.eu']
    TEST = '[TEST]'

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        tempfile.gettempdir(), 'us-census.db')
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URLS')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URLS')
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
