import datetime
from recipes.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import loader
from recipes.models import User, Recipe
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

@csrf_exempt
def login(request):
    form = UserCreationForm
    verify = 0
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        for user in User.objects.all():
            if user.email == request.POST.get('email'):
                if user.password == request.POST.get('password1'):
                    request.session['user'] = str(User.objects.get(userid=user.userid))
                    global diaryList
                    diaryList = []
                    return redirect("index")
                else:
                    verify = 1
                    break
            else:
                verify = 2
    context = {'form': form, 'verify': verify}
    return render(request, 'login.html', context)

@csrf_exempt
def recipes(request):
    recipe_list = Recipe.objects.all()
    #if('submit') in request.Post:
    if request.POST.get('AddTorecipie'):
        diaryList.append(request.POST.get('recipeInput'))
        print(request.POST.get('recipeInput'))
        print(diaryList[0])
        print("aaaaaahhhhhhh")
        
    
    return render(request, 'recipe.html', {'recipe_list' : recipe_list})

@csrf_exempt
def diary(request):
    recipe_list = Recipe.objects.all()
    #diary_list =
    totalCal = 0
    totalFat = 0
    totalSaturates = 0
    totalSugar = 0
    totalSalt = 0
    totalProtein = 0
    totalCarbs = 0
    totalFibre = 0
    for recipe in diaryList:
        recipetoo = Recipe.objects.get(nameOfRecipe = recipe)
        totalCal += recipetoo.calories
        totalFat += recipetoo.fat
        totalSaturates += recipetoo.saturates
        totalSugar += recipetoo.sugar
        totalSalt += recipetoo.salt
        totalProtein += recipetoo.protein
        totalCarbs += recipetoo.carbs
        totalFibre += recipetoo.fibre
            

    #Creation of the piechart     
    xdata = ["calories","fat","saturates","sugar","salt","protein","carbs","fibre"]
    ydata = [totalCal, totalFat, totalSaturates, totalSugar, totalSalt, totalProtein, totalCarbs, totalFibre]
    
   
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    
    return render(request, 'diary.html', data)

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