from flask import Flask, request, jsonify, Response
from models import User

app = Flask(__name__)

@app.route('/user', methods=['GET','POST','PUT','DELETE'])
@app.route('/user/<string:user_id>', methods=['GET','POST','PUT','DELETE'])
def user(user_id=None):
    if request.method == 'GET':
        users = User.objects()
        users_json = users.to_json()
        return Response(users_json, content_type='application/json')

    elif request.method == 'POST':
        print(request.json)
        u = User(**request.json)
        u.save()
        user_json = u.to_json()
        #return jsonify({'status':'created'})
        return Response(user_json, content_type='application/json')
    elif request.method == 'PUT' and user_id:
        u = User.objects().get(id=user_id)
        print(u)
        updated_users = u.update(**request.json)
        #return jsonify({'status': 'updated'})
        u.reload()
        return Response(u.to_json(), content_type='application/json')
    elif request.method == 'DELETE' and user_id:
        User.objects(id=user_id).delete()
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'status':'error'})

app.run(debug=True)