from  peewee import  *
db = SqliteDatabase("my_database.db")
class User(Model):
    names = CharField()
    email = CharField()
    age =IntegerField()
    password =CharField()
    class Meta:
        database =db
#User.create_table()
#User.create(names="John Mark",email="john@yahoo.com",age =13, password="123456")
# john = User.get(User.id == 1)
# print(john.names)

