from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import InstaUser
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View
# python 
# csrf --> cross site request forgery, phishig attcks
# Create your views here.
# print hello world
def hello_world(request):
    return HttpResponse('Hello World')

def another_func(request,id):
    return HttpResponse(f'Hello harsha your number is {id}')

@csrf_exempt
def usercreation(request):
    if request.method == 'POST':   # signup page form backend developers  
        id = request.POST['id']  # {'id':123}
        name = request.POST['name']
        location = request.POST['location']
        gender = request.POST['gender']
        modified_name = name + ' ' + 'VN2 Solutions'
        data = InstaUser(id = id, name = modified_name, location = location, gender = gender)  # data is an object of InstaUser
        data.save()
        return HttpResponse('Data created successfully',status = 201)

    elif request.method == 'GET':
        # SELECT * 
        # FROM instauser
        """
        SELECT "reels_instauser"."id", "reels_instauser"."name",
         "reels_instauser"."location", 
        "reels_instauser"."gender" 
        FROM "reels_instauser"
        """
        data = InstaUser.objects.all()  # queryset not query object
        print('....................',data.query)
        response_o = {}
        for each in data:
            print(each.name)
            response_o[each.id] = each.name
        return HttpResponse(f'data is  {response_o}',status = 200)

# @method_decorator(csrf_exempt)
class UserDetail(View):  # you just use whatever your company is using in the current project
    # do not hit database most of time, first create a query set 
    # if we use .filter it will return query set 
    # if we use .get it will return query object 
    # get_object_or_404 search for this and implment on your own
    def get(self,request,id):
        try:
            data = InstaUser.objects.get(id = id)
            return HttpResponse(f'user name is {data.name} and location is {data.location}',status = 200)
        except Exception as e:
            return HttpResponse('User with given id not found', status = 404)

    def post(self,request,id):
        data = InstaUser.objects.get(id = id)  # data is an object of InstaUser class, id name gender location
        location = request.POST['location']
        data.location  = location
        data.save()
        return HttpResponse('Data updated successfully',status = 200)
    
    def delete(self,request,id):
        data = InstaUser.objects.get(id = id)  # data is an object of InstaUser class, id name gender location
        data.delete()
        return HttpResponse('Data deleted successfully',status = 200)

"""
request --> request url --> www.xyz.com/reels/home
urls.py --> project have we included the urls of an application in the project
urls.py --> app  have we created api end point in urls.py for this view
views.py -> app have we implemented business logic in the views

GET PUT POST DELETE
POST to create data in the database 
table, columns

"""

# http://127.0.0.1:8000/reels/home/
# reels we are getting from project 
# home we are getting from application