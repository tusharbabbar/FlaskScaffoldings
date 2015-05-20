from flask.ext.restful import Resource

class HelloApi(Resource):
    def get(self):
        return {'hello' : 'api'}
