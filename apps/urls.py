from flask import Flask
from flask_restful import Api
# 预测车流量

from apps.main.apis import HomeApi

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


api.add_resource(HomeApi, '/home/')
