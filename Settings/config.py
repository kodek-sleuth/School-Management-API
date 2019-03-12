class Config():
    SECRET_KEY='its nolonger a secret'

class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    SQLALCHEMY_DATABASE_URI='postgresql://business:businessonly@localhost:5432/luqman'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 
    
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG=True
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:believe@localhost:5432/fortestsonly'

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:believe@localhost:5432/fortestsonly'
    SQLALCHEMY_TRACK_MODIFICATIONS=False 


app_config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}