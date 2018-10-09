from flask import Flask

from apps.settings import ProductConfig
from apps.ext import init_ext
from apps.settings import env
from apps.urls import init_api


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(env.get(env_name))
    init_ext(app)
    init_api(app)
    return app
