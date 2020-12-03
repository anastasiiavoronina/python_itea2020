from flask import Flask, request, jsonify, Response
from blog_models import Tag, Author, Post

app = Flask(__name__)


@app.route('/tag', methods=['GET','POST','PUT','DELETE'])
@app.route('/tag/<string:tag_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tag(tag_id=None):
    if request.method == 'GET':
        tags = Tag.objects()
        tags_json = tags.to_json()
        return Response(tags_json, content_type='application/json')
    elif request.method == 'POST':
        print(request.json)
        t = Tag(**request.json)
        t.save()
        tag_json = t.to_json()
        return Response(tag_json, content_type='application/json')
    elif request.method == 'PUT' and tag_id:
        t = Tag.objects().get(id=tag_id)
        print(t)
        t.update(**request.json)
        t.reload()
        return Response(t.to_json(), content_type='application/json')
    elif request.method == 'DELETE' and tag_id:
        Tag.objects(id=tag_id).delete()
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'status': 'error'})


@app.route('/author', methods=['GET','POST','PUT','DELETE'])
@app.route('/author/<string:author_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def author(author_id=None):
    if request.method == 'GET':
        authors = Author.objects()
        authors_json = authors.to_json()
        return Response(authors_json, content_type='application/json')
    elif request.method == 'POST':
        print(request.json)
        a = Author(**request.json)
        a.save()
        author_json = a.to_json()
        #return jsonify({'status':'created'})
        return Response(author_json, content_type='application/json')
    elif request.method == 'PUT' and author_id:
        a = Author.objects().get(id=author_id)
        print(a)
        a.update(**request.json)
        a.reload()
        return Response(a.to_json(), content_type='application/json')
    elif request.method == 'DELETE' and author_id:
        Author.objects(id=author_id).delete()
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'status': 'error'})

@app.route('/post', methods=['GET','POST','PUT','DELETE'])
@app.route('/post/<string:post_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post(post_id=None):
    if request.method == 'GET':
        if post_id:
            post = Post.objects().get(id=post_id)
            post.update(views_amount=post.views_amount + 1)
            post.reload()
            return Response(post.to_json(), content_type='application/json')
        else:
            posts = Post.objects()
            return Response(posts.to_json(), content_type='application/json')
    elif request.method == 'POST':
        print(request.json)
        p = Post(**request.json)
        p.save()
        a = p.author
        a.update(posts_amount=a.posts_amount+1)
        post_json = p.to_json()
        return Response(post_json, content_type='application/json')
    elif request.method == 'PUT' and post_id:
        p = Post.objects().get(id=post_id)
        print(p)
        print(request.json)
        old_author_id = p.author.id
        p.update(**request.json)
        p.reload()
        new_author_id = p.author.id
        if old_author_id != new_author_id:
            a_old = Author.objects().get(id=old_author_id)
            a_old.update(posts_amount=a_old.posts_amount-1)
            a_new = Author.objects().get(id=new_author_id)
            a_new.update(posts_amount=a_new.posts_amount + 1)
        return Response(p.to_json(), content_type='application/json')
    elif request.method == 'DELETE' and post_id:
        p = Post.objects().get(id=post_id)
        a = p.author
        a.update(posts_amount=a.posts_amount-1)
        p.delete()
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'status': 'error'})

@app.route('/posts_by_tag')
@app.route('/posts_by_tag/<string:tag_id>')
def posts_by_tag(tag_id=None):
    if request.method == 'GET':
        tags = Tag.objects(id=tag_id)
        if len(tags) == 1:
            posts = Post.objects(tag=tags[0])
            posts_json = posts.to_json()
            return Response(posts_json, content_type='application/json')
        else:
            return jsonify({'status': 'There are no posts with such tag'})

@app.route('/posts_by_author')
@app.route('/posts_by_author/<string:author_id>')
def posts_by_author(author_id=None):
    if request.method == 'GET':
        authors = Author.objects(id=author_id)
        if len(authors) == 1:
            posts = Post.objects(author=authors[0])
            posts_json = posts.to_json()
            return Response(posts_json, content_type='application/json')
        else:
            return jsonify({'status': 'There are no posts with such author'})


app.run(debug=True)