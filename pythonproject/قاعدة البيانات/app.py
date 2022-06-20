from Model import Model
from Field import *
from Database import Database

Model.db= Database('database.sqlite')
Model.connection=Model.db.connect()

class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DataTimeField()
    published = BooleanField()

class User(Model):
    first_name = CharField()
    last_name =CharField(max_length=255)
    age = IntegerField()


if __name__ == '__main__':
    post = Post()

