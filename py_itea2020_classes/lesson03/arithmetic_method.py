class News:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __add__(self, other):
        new_title = self.title + other.title
        new_body = self.body + other.body
        return News(new_title, new_body)

    def __str__(self):
        return f'Title is {self.title}\nBody is {self.body}'

news1 = News('Football','.........')
news2 = News('Hockey', ',,,,,,')
news3 = News('Coronavirus', '--------')

r = news1 + news2 + news3
print(r)

