
class Config(object):
    '''
    Common Configurations
    '''

class DevelopmentConfig(Config):
    '''
    Development Config
    '''
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    '''
    ProductionConfig
    '''
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}
