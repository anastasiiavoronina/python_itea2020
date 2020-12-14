from flask import Flask, request, jsonify, Response
from flask_restful import Api
from resources import TagResource, AuthorResource, PostResource, PostsByTagResource, PostsByAuthorResource


app = Flask(__name__)
api = Api(app)

api.add_resource(TagResource, '/tag', '/tag/<string:id>')
api.add_resource(AuthorResource, '/author', '/author/<string:id>')
api.add_resource(PostResource, '/post', '/post/<string:id>')
api.add_resource(PostsByTagResource, '/posts_by_tag/<string:tag_id>')
api.add_resource(PostsByAuthorResource, '/posts_by_author/<string:author_id>')


app.run(debug=True)