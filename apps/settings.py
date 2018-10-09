# debug = True
DATABASES_DEFAULT_KEY = 'default'
DATABASES_DEFAULT_ENGINE = 'mysql'
DATABASES_DEFAULT_DRIVER = 'pymysql'
DATABASES_DEFAULT_PORT = '3306'
DATABASES_DEFAULT_HOST = '127.0.0.1'
DATABASES_DEFAULT_CHARSET = 'utf8'


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 秘钥
    SECRET_KEY = '21039c08cac511e882c5001c42de2dd9'


DATABASES = {
    'default': {
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'tpp',

    },
    'pro': {
        'ENGINE': 'mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'tpp',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    },
}


# 生成数据库连接的路径
def get_db_uri(key=None):
    database_config = DATABASES.get(key) if key else DATABASES.get(DATABASES_DEFAULT_KEY)
    engine = database_config.get('ENGINE') or DATABASES_DEFAULT_ENGINE
    driver = database_config.get('DRIVER') or DATABASES_DEFAULT_DRIVER
    host = database_config.get('HOST') or DATABASES_DEFAULT_HOST
    port = database_config.get('PORT') or DATABASES_DEFAULT_PORT
    user = database_config.get('USER')
    password = database_config.get('PASSWORD')
    name = database_config.get('NAME')
    charset = database_config.get('CHARSET') or DATABASES_DEFAULT_CHARSET
    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{name}?charset={charset}'


# 部署的环境
class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = get_db_uri('pro')


# 开发环境
class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_uri()


DEVELOP = 'dev'
PRODUCT = 'pro'

env = {
    DEVELOP: DevelopConfig,
    PRODUCT: ProductConfig
}
