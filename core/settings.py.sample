import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Default(object):
    DEBUG = False
    TESTING = False
    SECRET = 'ChronosBestKeptSecret'


class Development(Default):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/Chronos'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    MAILGUN_DOMAIN = 'sandbox046614b25f374c168de8c9651c06dc89.mailgun.org'
    MAILGUN_KEY = 'key-ed12489643a0a9db3e080779200a2d2e'
    API_SIGNING_KEY = 'SigningKeyForChronosApi'
    REDIS_HOST = 'localhost'
    REDIS_DB = 0


class Production(Default):
    DEBUG = False


class Testing(Default):
    DEBUG = True
    TESTING = True
