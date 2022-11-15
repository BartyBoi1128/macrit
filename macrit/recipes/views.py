import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import loader
from recipes.models import Profile, User
from recipes.service import *

# Create your views here.

# testUser = User.objects.get(userid=19269609)
# testProfile = Profile.objects.create(user=testUser, first_name="Ivanna", second_name="Tinkle", height=183, weight=250,BMI=bmiCalc(183, 250),age=22,gender=False,weight_goal=200,weight_goal_time=datetime.datetime(2022, 12, 12),vegeterian=True, vegan=False)


def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def diary(request):
    return render(request, 'diary.html')

def register(request):
    form = UserCreationForm
    context = {'form': form}
    return render(request, 'register.html', context)