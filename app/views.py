from app import app
from flask import  render_template,make_response,request,jsonify
from flask_restful import Resource, Api
from app import models
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from datetime import timedelta

api = Api(app)

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return (user)

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA']=timedelta(seconds=30)
jwt = JWT(app, authenticate, identity) 
class HelloWorld(Resource):
    decorators = [jwt_required()]
    def get(self):
        queryset = models.Table3.query.all()
        return make_response(render_template('base.html', details = queryset),200)

	
api.add_resource(HelloWorld, '/')

