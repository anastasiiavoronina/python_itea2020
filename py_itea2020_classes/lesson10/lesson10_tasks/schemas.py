from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length, Range


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=128), required=True)
    last_name = fields.String(validate=Length(min=2, max=128), required=True)
    posts_amount = fields.Int(default=0, dump_only=True)


class TagSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=Length(min=2, max=64), required=True)


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    subject = fields.String(validate=Length(min=2, max=256), required=True)
    content = fields.String(validate=Length(min=2, max=4000))
    published = fields.DateTime(format="%b %d %Y %H:%M:%S")
    author = fields.Nested(AuthorSchema)
    tag = fields.Nested(TagSchema)
    views_amount = fields.Int(default=0, dump_only=True)


class PostSchemaWrite(Schema):
    id = fields.String(dump_only=True)
    subject = fields.String(validate=Length(min=2, max=256), required=True)
    content = fields.String(validate=Length(min=2, max=4000))
    published = fields.DateTime(format="%b %d %Y %H:%M:%S")
    author = fields.String(required=True)
    tag = fields.String(required=True)
    views_amount = fields.Int(default=0, dump_only=True)
