import mongoengine as me
import random
from datetime import datetime, timedelta

me.connect('rest_api_lesson10_blog')

first_names = ['Nikolai', 'Tom', 'Ann', 'Robin', 'Jane', 'Mary', 'Jerry']
last_names = ['Simpson', 'Trump', 'Doe', 'Dickens', 'Richards', 'Roberts', 'Grant']
subjects = [('Cooking',
            ['recipe for cooking borsch', 'recipe for cooking greek salad', 'recipe for cooking cake'],
            ['fish', 'meat', 'fruits', 'vegetables']),
            ('Movies',
             ['New movie called Superintelligence', 'New movie Black Box', 'New movie The Retched',
              'New movie Mulan', 'New movie The Gentlemen'],
             ['comedy', 'detective', '2020', '2021']),
            ('Business',
             ['Taxes to be increased', 'Salary to be increased',
              'Small business suffering from the quarantine', 'Changes in taxes'],
             ['quarantine', 'taxes', 'law', 'salary']),
            ('Medicine',
             ['Vaccine from covid has been invented', 'Quarantine coming soon', 'Covid vaccine testing'],
             ['quarantine', 'coronavirus', 'covid', 'vaccine'])]


class Author(me.Document):
    first_name = me.StringField(required=True, min_length=2, max_length=128)
    last_name = me.StringField(required=True, min_length=2, max_length=128)
    posts_amount = me.IntField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(me.Document):
    name = me.StringField(required=True, unique=True, min_length=2, max_length=64)

    def __str__(self):
        return f'{self.name}'


class Post(me.Document):
    subject = me.StringField(required=True, min_length=2, max_length=256)
    content = me.StringField(min_length=2, max_length=4000)
    published = me.DateTimeField()
    author = me.ReferenceField(Author, reverse_delete_rule=me.NULLIFY)
    tag = me.ReferenceField(Tag, reverse_delete_rule=me.NULLIFY)
    views_amount = me.IntField(default=0)

    def __str__(self):
        return f'{self.subject}: {self.content}. Published: {str(self.published)}. Author ' + \
               self.author.first_name + ' ' + self.author.last_name + '. Tag: ' + self.tag.name


def add_data_to_db(posts_amount=10):
    authors_amount = round(posts_amount/3)
    new_authors = []
    for i in range(authors_amount):
        author_first_name = first_names[random.randint(0, len(first_names)-1)]
        author_last_name = last_names[random.randint(0, len(last_names)-1)]
        a = Author(first_name=author_first_name, last_name=author_last_name)
        print(a)
        a.save()
        new_authors.append(a)

    for i in range(posts_amount):
        post_info = subjects[random.randint(0, len(subjects)-1)]
        post_subject = post_info[0]
        post_content = post_info[1][random.randint(0, len(post_info[1])-1)]
        post_author = new_authors[random.randint(0, len(new_authors)-1)]
        published_date = datetime.today() - timedelta(days=random.randint(0, 180))
        tag_name = post_info[2][random.randint(0, len(post_info[2])-1)]
        tag = Tag.objects(name=tag_name)
        if len(tag) == 0:
            post_tag = Tag(name=tag_name)
            post_tag.save()
        else:
            post_tag = tag[0]
        p = Post(subject=post_subject, content=post_content, published=published_date, author=post_author, tag=post_tag)
        print(p)
        p.save()
        post_author.update(posts_amount=post_author.posts_amount+1)


if __name__ == '__main__':

    add_data_to_db()