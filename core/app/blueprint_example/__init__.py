from flask import Blueprint 
from flask.ext import restful
from app import *

my_blueprint = Blueprint('my_blueprint', __name__, url_prefix='/my_blueprint')

api = restful.Api(my_blueprint)

### add resources to api.
from app.blueprint_example.resources import *
api.add_resource(HelloBluePrint, '/helloblu')
