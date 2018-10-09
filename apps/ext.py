from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from flask_cors import CORS

def init_ext(app):
    init_db(app)
    init_cors(app)


db = SQLAlchemy()
migrate = Migrate()


# 初始化db
def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)


#初始化跨域请求
def init_cors(app):
    pass