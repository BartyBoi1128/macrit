import datetime
from recipes.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import loader
from recipes.models import User
from recipes.service import *
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

# Create your views here.

# testUser = User.objects.get(userid=19269609)
# testProfile = Profile.objects.create(user=testUser, first_name="Ivanna", second_name="Tinkle", height=183, weight=250,BMI=bmiCalc(183, 250),age=22,gender=False,weight_goal=200,weight_goal_time=datetime.datetime(2022, 12, 12),vegeterian=True, vegan=False)


def index(request):
    if 'user' in request.session:
        user = request.session['user']
    return render(request, 'index.html', {})

def settings(request):
    return render(request,'index.html', {})

def login(request):
    form = UserCreationForm
    verify = 0
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        for user in User.objects.all():
            if user.email == request.POST.get('email'):
                if user.password == request.POST.get('password1'):
                    request.session['user'] = str(User.objects.get(userid=user.userid))
                    return redirect("index")
                else:
                    verify = 1
                    break
            else:
                verify = 2
    context = {'form': form, 'verify': verify}
    return render(request, 'login.html', context)

@csrf_exempt
def register(request):
    form = UserCreationForm
    
    #cookies = {'csrftoken'}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password1')
            User.objects.create(email = email, password = password)
            return redirect("login")

    context = {'form': form}
    return render(request, 'register.html', context)