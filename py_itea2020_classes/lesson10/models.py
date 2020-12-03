import mongoengine as me

me.connect('rest_api_test_lesson10')

class UserProfile(me.Document):
    login = me.StringField(required=True, unique=True, min_length=4, max_length=128)
    password = me.StringField(required=True, min_length=8)
    about_me = me.StringField()
    likes = me.IntField(default=0)

    def __str__(self):
        return str(self.id)

class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()
    user_profile = me.ReferenceField(UserProfile)

if __name__ == '__main__':
    User.objects().delete()
    up = UserProfile(login = 'addadfadfa', password='dfdreree')
    up.save()
    #up.reload()
    user = User(first_name='Nikolai', interests=['cars'], age=28, user_profile = up)
    user.save()
    user = User(first_name='Mike', interests=['swimming'], age=38, user_profile = up)
    user.save()