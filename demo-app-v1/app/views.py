from app import app
"""
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
"""
from flask_restful import Resource, Api
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

