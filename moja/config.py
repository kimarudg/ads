import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
mediapath='/externaldrive/'
mediadir = os.path.abspath(os.path.dirname(mediapath))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7aHzKo9FMHxKcu+123M'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    DOWNLOAD_DIR = os.environ.get('DOWNLOAD_PATH_URL') or os.path.join(mediadir, '/downloads')
    POST_SYNC_SCRIPT = 'python /usr/share/moja/manage.py post-sync'
    URL_CHECKER = 'https://www.simiti.io/api/v2/devices'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'simiti.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INFO_LOG_PATH = os.environ.get('ERROR_LOG_PATH_URL') or os.path.join(basedir, 'infofile.log')
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=5)

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'simiti.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INFO_LOG_PATH = os.environ.get('ERROR_LOG_PATH_URL') or os.path.join(basedir, 'infofile.log')
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=5)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'simiti.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INFO_LOG_PATH = os.environ.get('ERROR_LOG_PATH_URL') or os.path.join(mediadir, '/logs/INFOfile.log')
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=5)

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}
