from flask_restful import Resource
from flask import request
from blog_models import Tag, Author, Post
import json
from schemas import TagSchema, AuthorSchema, PostSchema, PostSchemaWrite
from marshmallow.exceptions import ValidationError


class TagResource(Resource):

    def get(self, id=None):
        if id:
            return TagSchema().dump(Tag.objects.get(id=id))
        else:
            tags = Tag.objects()
            return json.loads(tags.to_json())

    def post(self):
        try:
            TagSchema().load(request.json)
        except ValidationError as e:
            return {'error': str(e)}
        t = Tag(**request.json)
        t.save()
        return TagSchema().dump(t)

    def put(self, id=None):
        if id:
            try:
                TagSchema().load(request.json)
            except ValidationError as e:
                return {'error': str(e)}
            t = Tag.objects().get(id=id)
            t.update(**request.json)
            t.reload()
            return TagSchema().dump(t)
        else:
            return {'status': 'id of deleted object is not specified'}

    def delete(self, id=None):
        if id:
            Tag.objects(id=id).delete()
            return {'status': 'deleted'}
        else:
            return {'status': 'id of deleted object is not specified'}


class AuthorResource(Resource):

    def get(self, id=None):
        if id:
            return AuthorSchema().dump(Author.objects.get(id=id))
        else:
            authors = Author.objects()
            return json.loads(authors.to_json())

    def post(self):
        try:
            AuthorSchema().load(request.json)
        except ValidationError as e:
            return {'error': str(e)}
        a = Author(**request.json)
        a.save()
        return AuthorSchema().dump(a)

    def put(self, id=None):
        if id:
            try:
                AuthorSchema().load(request.json)
            except ValidationError as e:
                return {'error': str(e)}
            a = Author.objects().get(id=id)
            a.update(**request.json)
            a.reload()
            return AuthorSchema().dump(a)
        else:
            return {'status': 'id of deleted object is not specified'}

    def delete(self, id=None):
        if id:
            Author.objects(id=id).delete()
            return {'status': 'deleted'}
        else:
            return {'status': 'id of deleted object is not specified'}


class PostResource(Resource):

    def get(self, id=None):
        if id:
            post = Post.objects().get(id=id)
            post.update(views_amount=post.views_amount + 1)
            post.reload()
            return PostSchema().dump(post)
        else:
            posts = Post.objects()
            return json.loads(posts.to_json())

    def post(self):
        try:
            PostSchema().load(request.json)
        except ValidationError as e:
            return {'error': str(e)}
        post_params = request.json
        post_params['author'] = Author.objects().get(id=post_params['author'])
        post_params['tag'] = Tag.objects().get(id=post_params['tag'])
        p = Post(**post_params)
        p.save()
        a = p.author
        a.update(posts_amount=a.posts_amount+1)
        return PostSchema().dump(p)

    def put(self, id=None):
        if id:
            try:
                PostSchemaWrite().load(request.json)
            except ValidationError as e:
                return {'error': str(e)}
            p = Post.objects().get(id=id)
            old_author_id = p.author.id
            post_params = request.json
            post_params['author'] = Author.objects().get(id=post_params['author'])
            post_params['tag'] = Tag.objects().get(id=post_params['tag'])
            p.update(**post_params)
            p.reload()
            new_author_id = p.author.id
            if old_author_id != new_author_id:
                a_old = Author.objects().get(id=old_author_id)
                a_old.update(posts_amount=a_old.posts_amount - 1)
                a_new = Author.objects().get(id=new_author_id)
                a_new.update(posts_amount=a_new.posts_amount + 1)
            return PostSchema().dump(p)
        else:
            return {'status': 'id of deleted object is not specified'}

    def delete(self, id=None):
        if id:
            p = Post.objects().get(id=id)
            a = p.author
            a.update(posts_amount=a.posts_amount - 1)
            p.delete()
            return {'status': 'deleted'}
        else:
            return {'status': 'id of deleted object is not specified'}


class PostsByTagResource(Resource):

    def get(self, tag_id=None):
        tags = Tag.objects(id=tag_id)
        if len(tags) == 1:
            posts = Post.objects(tag=tags[0])
            return PostSchema().dump(posts, many=True)
        else:
            return {'status': 'There is no such tag'}


class PostsByAuthorResource(Resource):

    def get(self, author_id=None):
        authors = Author.objects(id=author_id)
        if len(authors) == 1:
            posts = Post.objects(author=authors[0])
            return PostSchema().dump(posts, many=True)
        else:
            return {'status': 'There is no such author'}
