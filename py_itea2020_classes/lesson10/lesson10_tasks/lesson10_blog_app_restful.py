from flask import Flask, request, jsonify, Response
from flask_restful import Api
from resources import TagResource, AuthorResource, PostResource, PostsByTagResource, PostsByAuthorResource
#from blog_models import Tag, Author, Post

app = Flask(__name__)
api = Api(app)

api.add_resource(TagResource, '/tag', '/tag/<string:id>')
api.add_resource(AuthorResource, '/author', '/author/<string:id>')
api.add_resource(PostResource, '/post', '/post/<string:id>')
api.add_resource(PostsByTagResource, '/posts_by_tag/<string:tag_id>')
api.add_resource(PostsByAuthorResource, '/posts_by_author/<string:author_id>')

# @app.route('/posts_by_tag')
# @app.route('/posts_by_tag/<string:tag_id>')
# def posts_by_tag(tag_id=None):
#     if request.method == 'GET':
#         tags = Tag.objects(id=tag_id)
#         if len(tags) == 1:
#             posts = Post.objects(tag=tags[0])
#             posts_json = posts.to_json()
#             return Response(posts_json, content_type='application/json')
#         else:
#             return jsonify({'status': 'There are no posts with such tag'})
#
# @app.route('/posts_by_author')
# @app.route('/posts_by_author/<string:author_id>')
# def posts_by_author(author_id=None):
#     if request.method == 'GET':
#         authors = Author.objects(id=author_id)
#         if len(authors) == 1:
#             posts = Post.objects(author=authors[0])
#             posts_json = posts.to_json()
#             return Response(posts_json, content_type='application/json')
#         else:
#             return jsonify({'status': 'There are no posts with such author'})

app.run(debug=True)