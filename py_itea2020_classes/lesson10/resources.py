from flask_restful import Resource
from flask import request
from models import User
import json
from Schemas import UserSchema
from marshmallow.exceptions import ValidationError

class UserResource(Resource):

    def get(self, id=None):
        if id:
            return UserSchema().dump(User.objects.get(id=id))
        else:
            users = User.objects()
            return json.loads(users.to_json())

    def post(self):

        try:
            UserSchema().load(request.json)
        except ValidationError as e:
            return {'error':str(e)}
        print(s)
        u = User(**request.json)
        u.save()
        return UserSchema().dump(user) #json.loads(u.to_json())

    def put(self):
        pass

    def delete(self):
        pass