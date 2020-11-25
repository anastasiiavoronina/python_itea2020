import mongoengine as me

me.connect('test_mongo_db_lesson09')

class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)


if __name__ == '__main__':
    #user = User(first_name='Michael', interests=['Swimming', 'Programming'], age=38)
    #user.save()
    #users = User.objects(first_name='John')
    #users = User.objects(first_name__ne='John')
    #users = User.objects(age__in=[18,21])
    users = User.objects(age__gte=18, first_name='John')
    print(users)
    for u in users:
        print(u.first_name, u.last_name, u.interests, u.age)