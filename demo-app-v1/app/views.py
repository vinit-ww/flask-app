from app import app
from flask import  render_template,make_response
from flask_restful import Resource, Api
from app import models

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        queryset = models.Table3.query.all()
        return make_response(render_template('base.html', details = queryset),200)


api.add_resource(HelloWorld, '/')

