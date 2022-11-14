from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponse, redirect, render
from django.template import loader
from recipes.models import Profile, User
from recipes.service import *

# Create your views here.

# testUser = User.objects.create(password="safepass", email="useremail@gmail.com")
# testProfile = Profile.objects.create(user=testUser, first_name="Ivanna", second_name="Tinkle", height=183, weight=250,BMI=bmiCalc(Profile.height,Profile.weight),age=22,gender=False,weight_goal=200,weight_goal_time="12/12/2022",vegeterian=True, vegan=False)

def index(request):
    return render(request, 'recipes/index.html', {'element_id': "index"})

def settings(request):
    return render(request,'recipes/index.html', {'element_id': "settings"})

def login(request):
    context = {}
    return render(request, 'recipes/login.html', context)#{'element_id': "login"})

def register(request):
    form = UserCreationForm
    context = {'form': form}
    return render(request, 'recipes/register.html', context)#{'element_id': "register"})