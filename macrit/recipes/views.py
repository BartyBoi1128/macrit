import datetime
from recipes.forms import UserCreationForm, registerProfileForm
from django.shortcuts import redirect, render
from django.template import loader
from recipes.models import User, Profile, Recipe
from recipes.service import *
from recipes.usersettings import *
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
                    request.session['user'] = str(User.objects.get(userid = user.userid).userid)
                    return redirect("index")
                else:
                    verify = 1
                    break
            else:
                verify = 2
    context = {'form': form, 'verify': verify}
    return render(request, 'login.html', context)

def recipes(request):
    recipe_list = Recipe.objects.all()
    
    
    # if request.method == "POST":
    #     form = 
    #     if request.POST.get(""):
    #         return
    return render(request, 'recipe.html', {'recipe_list' : recipe_list})
#Bart
       # self.profile_age = newAge
       # self.profile_gender = newGender
       # self.profile_weight = newWeight
       # self.profile_height = newHeight
       # self.profile_weight_goal = newGoal
       # self.profile_weight_goal_time = newGoalTime
       # self.profile_bmi = bmiCalc(self.profile_height, self.profile_weight)
def settings(request):
    current_user = User.objects.get(userid = request.session['user'])
    current_settings = usersettings()
    #Finish this after profile page
    #if not hasattr('current_user', 'profile'):
    #    new_profile = Profile()
    #    current_user.setProfile(current_user, new_profile)
    current_settings.setAll(current_settings, current_user.profile.age, current_user.profile.gender, current_user.profile.weight, current_user.profile.height, current_user.profile.weight_goal, current_user.profile.weight_goal_time)
    current_settings.attach(current_settings, current_user.profile)
    contexttings = {
        'age': current_user.age,
        'gender': current_user.gender
    }
    return render(request, 'settings.html', contexttings)

#Bart
#first_name = models.CharField(max_length=50)
	#second_name = models.CharField(max_length=100)
	#height = models.FloatField()
	#weight = models.FloatField()
	#BMI = models.FloatField()
	#age = models.IntegerField()
	#gender = models.BooleanField(default=False)
	#weight_goal = models.FloatField()
	#weight_goal_time = models.DateField()
	#vegeterian = models.BooleanField(default=False)
	#vegan = models.BooleanField(default=False)
def registerProfile(request):
    if request.method == "POST":
        form = registerProfileForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            sn = form.cleaned_data["second_name"]
            h = form.cleaned_data["height"]
            w = form.cleaned_data["weight"]
            a = form.cleaned_data["age"]
            g = form.cleaned_data["gender"]
            wg = form.cleaned_data["weight_goal"]
            wgt = form.cleaned_data["weight_goal_time"]
            vgt = form.cleaned_data["vegeterian"]
            vg = form.cleaned_data["vegan"]
            Profile.objects.create(first_name = fn, second_name = sn, height = h, weight = w, BMI= bmiCalc(h,w), age = a, gender = g, weight_goal = wg, weight_goal_time = wgt, vegeterian = vgt, vegan = vg, user = User.objects.get(userid = request.session['user']))           
            return redirect("login")
    else:
        form = registerProfileForm()        
        return render(request, 'registerProfile.html', {"form":form})

@csrf_exempt
def register(request):
    form = UserCreationForm
    
    #cookies = {'csrftoken'}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            e_mail = request.POST.get('email', '')
            password = request.POST.get('password1')
            User.objects.create(email = e_mail, password = password)
            request.session['user'] = User.objects.get(email=e_mail).userid
            return redirect("registerProfile")
    context = {'form': form}
    return render(request, 'register.html', context)