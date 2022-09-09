"""
file structure and work flow 
MVT --> Model View Template 
ORM --> Object relational mapper --> objects of python is mapped to the relation of database 
class Employee():
    pass
emp_obj = Employee()
Model --> Rows and columns --> database tables --> we will crete database tables and columns 
View --> we wil implenet business logic, there are two types of views , class based view and function based view
Template  --> static files html css javascript 

instagram  # root folder 
    Instagram  # project package
        __init__.py
        asgi.py  # asynchronous gate way interface 
        wsgi.py  # webserver gate way interface
        settings.py # we will modify the settings of our project, Installed apps, Databases, Middleware
        urls.py   # we will specify api end points 
    reels
        templates
            reels 
                index.html
        __init__.py
        apps.py  # 
        views.py #
        models.py # 
        urls.py*
        admin.py
        tests.py
    manage.py





"""