class FlaskConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    '''
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT	= 20
    SQLALCHEMY_POOL_RECYCLE	= 3600
    SQLALCHEMY_MAX_OVERFLOW	= 50
    '''