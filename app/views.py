from app import app
from flask import render_template,make_response
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
        return make_response(render_template('index.html'))

api.add_resource(HelloWorld, '/')

