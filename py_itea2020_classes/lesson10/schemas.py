from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length, Range

class UserProfileSchema(Schema):
    id = fields.String()
    login = fields.String()
    password = fields.String(load_only=True)
    about_me = fields.String()
    likes = fields.Int(default=0)

class UserSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=64), required=True)
    interests = fields.List(fields.String)
    age = fields.Integer(validate=Range(min=12, max=99), load_only=True)
    created_at = fields.DateTime()
    user_profile = fields.Nested(UserProfileSchema)#fields.String()

class UserSchemaRead(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=64), required=True)
    interests = fields.List(fields.String)
    age = fields.Integer(validate=Range(min=12, max=99), load_only=True)
    created_at = fields.DateTime()
    user_profile = fields.Nested(UserProfileSchema)#fields.String()

class UserSchemaWrite(UserSchemaRead):
    user_profile = fields.String()
