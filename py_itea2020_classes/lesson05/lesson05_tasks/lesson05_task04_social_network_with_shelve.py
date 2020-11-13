from datetime import datetime
import shelve

class Authorization:

    _FILE_USERS = 'USERS'
    _posts = []

    def _logout(self):
        self._is_authorized = False
        self._current_user = ''
        self._current_user_is_admin = False

    def logout(self):
        self._logout()
        print('You are now logged out')

    def __init__(self):
        self._logout()

    def check_login_is_available(self, user):
        result = True
        try:
            with shelve.open(self.__class__._FILE_USERS) as db:
                if db[user]:
                    result = False
        except KeyError:
            result = True
        return result

    def check_password_is_valid(self, password):
        if len(password) >= 8 and any(chr.isdigit() for chr in password) and any(chr.isalpha() for chr in password):
            return True
        else:
            return False

    def register(self, user, password, password_confirmation, is_admin):
        if len(user) == 0 or len(password) == 0 or len (password_confirmation) == 0:
            print("User, password or password confirmation wasn't specified")
        elif password != password_confirmation:
            print("Passwords don't match")
        elif self.check_login_is_available(user) == False:
            print('User with such username already exists')
        else:
            with shelve.open(self.__class__._FILE_USERS) as db:
                db[user] = {'password': password,
                            'registration_date': datetime.now(),
                            'is_admin': is_admin}
            print('Registration successful')

    def login(self, user, password):
        try:
            with shelve.open(self.__class__._FILE_USERS) as db:
                if db[user]['password'] == password:
                    self._is_authorized = True
                    self._current_user = user
                    self._current_user_is_admin = db[user]['is_admin']
                    print(f'You are now logged in as {user}')
                else:
                    print("Combination of user/password doesn't exist")
        except KeyError:
            print("Combination of user/password doesn't exist")


class User(Authorization):

    def create_post(self, content):
        if self._is_authorized:
            self.__class__._posts.append(Post(self._current_user, content))
            print(f'Post "{content}" has been created')
        else:
            print("You can't create post until authorized")

    def print_users_info(self):
        if self._is_authorized:
            if self._current_user_is_admin:
                print('***Users Report***')
                with shelve.open(self.__class__._FILE_USERS) as db:
                    for u in db.keys():
                        print(f"    User name: {u}, registered: {str(db[u]['registration_date'])}")
                        for p in Authorization._posts:
                            if p._author == u:
                                print(f'        Post : {p._content}, publish date: {str(p._publish_date)}')
            else:
                print("Only admins can have users information")
        else:
            print("You can't get users information until authorized")


class Post:

    def __init__(self, author, content):
        self._publish_date = datetime.now()
        self._author = author
        self._content = content


user1 = User()
user1.register('u1','rt5tyi84j54','rooooooo',False)
user1.register('u1','rt5tyi84j54','rt5tyi84j54', False)
user1.register('u2','ghty78kjuiu','ghty78kjuiu', True)
user1.register('u3','ir63mhjr64','ir63mhjr64', False)
user1.login('u1','rt5tyi84j54yyy')
user1.create_post('my post 001')
user1.login('u1','rt5tyi84j54')
user1.create_post('my post 001')
user1.create_post('my post 003')
user1.logout()
user1.login('u3','ir63mhjr64')
user1.create_post('my post 004')
user1.print_users_info()
user1.logout()
user1.print_users_info()
user1.login('u2','ghty78kjuiu')
user1.create_post('my post 005')
user1.create_post('my post 006')
user1.create_post('my post 007')
user1.print_users_info()