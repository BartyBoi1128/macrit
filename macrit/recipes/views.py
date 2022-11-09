from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from models import User
from models import Profile
from controller import *
# Create your views here.
#from django.http import HttpResponse

testUser = User.objects.create(userid=19235305, password="safepass", email="useremail@gmail.com")
testProfile = Profile.objects.create(user=testUser, first_name="Ivanna", second_name="Tinkle", height=183, weight=250,BMI=bmiCalc(Profile.height,Profile.weight),age=22,gender=False,weight_goal=200,weight_goal_time="12/12/2022",vegeterian=True, vegan=False)

def index(request):
    #return render(request, 'recipes/index.html')
    template = loader.get_template('recipes/index.html')
    return HttpResponse(template.render())
    #return render(request, 'settings.html')