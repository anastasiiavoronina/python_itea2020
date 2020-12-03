import mongoengine as me

me.connect('user_info_bot_lesson11')


class UserInfo(me.Document):
    fio = me.StringField()
    phone = me.StringField()
    email = me.StringField()
    address = me.StringField()
    suggestions = me.StringField()

    def __str__(self):
        return str(self.fio)
