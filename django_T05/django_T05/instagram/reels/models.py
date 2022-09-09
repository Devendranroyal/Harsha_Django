from django.db import models

# Create your models here.

# orm object 

"""
models are used to create a table and columns in the database by using orm we will convert
python object to relation of database
ORM --> object relational mapper 

python manage.py makemigrations --> to create a revision file 0001_initial.py, this will not show the changes in the database 
python manage.py migrate --> this will reflect changes to the database

"""

class InstaUser(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length = 5, default= None)





"""

class Main:
    def save(self):
        return 'hello harsha'
class User(Main):
    age = 20
    def __init__(self,id,name):
        self.id = id 
        self.name = name 
    def save(self):
        return 'bye harsha '
user_obj = User(id = 12,name = 'harsha')

user_obj.id = 20


"""



# instauser 
# columns --> id  name location 