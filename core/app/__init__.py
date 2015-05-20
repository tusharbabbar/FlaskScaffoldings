from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from settings import basedir
from celery import Celery
from redis import Redis

import os

### Creating an instance of app.
app = Flask(__name__)

### Getting settings for the app.
app.config.from_object('settings.Development')

### initailizing a restful api with app.
api = restful.Api(app)

### setting up connection with sqlalchemy
db = SQLAlchemy(app)

### setting up loginmanager
lm = LoginManager()
lm.init_app(app)

### setting up celery
cel = Celery(broker = app.config['CELERY_BROKER_URL'])

### setting up redis
red = Redis(app.config['REDIS_HOST'], db = app.config['REDIS_DB'])

### adding blueprints to app
from app.blueprint_example import my_blueprint
app.register_blueprint(my_blueprint)

### adding resources to rest api
from app.resources import *

api.add_resource(HelloApi, "/helloapi")


if __name__ == '__main__':
        app.run()
