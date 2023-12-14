class Config():
    SECRET_KEY = '2ae0a61787937e86297484b3051424dc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'

    HOST = '0.0.0.0'
    PORT = 5001

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass