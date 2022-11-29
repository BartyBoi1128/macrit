import datetime
from recipes.forms import UserCreationForm, registerProfileForm, userSettingsForm
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

    #profile_age = forms.FloatField(label= "Age")
    #profile_gender = forms.BooleanField(label= "Male?")
    #profile_weight = forms.FloatField(label= "Weight")
    #profile_height = forms.FloatField(label= "Height")
    #profile_weight_goal = forms.FloatField(label= "Weight Goal")

    #profile_weight_goal_time = forms.DateField(label= "Weight Goal Time")
def settings(request):
    if request.method == "POST":
        form = userSettingsForm(request.POST)
        current_settings = usersettings()
        if form.is_valid():
            pa = form.cleaned_data["profile_age"]
            pg = form.cleaned_data["profile_gender"]
            pw = form.cleaned_data["profile_weight"]
            ph = form.cleaned_data["profile_height"]
            pwg = form.cleaned_data["profile_weight_goal"]
            pwgt = form.cleaned_data["profile_weight_goal_time"]
            for profile in Profile.objects.all():
                if profile.user == User.objects.get(userid = request.session['user']):
                    print(pa)
                    if pa == None:
                        pa = profile.age
                    if pg == False:
                        pg = profile.gender
                    else:
                        pg = not profile.gender                   
                    if pw == None:
                        pw = profile.weight
                    if ph == None:
                        ph = profile.height
                    if pwg == None:
                        pwg = profile.weight_goal
                    if pwgt == None:
                        pwgt = profile.weight_goal_time 
                    current_settings.setAll(pa, pg, pw, ph, pwg, pwgt)
                    current_settings.attach(profile)
                    current_settings.notify()
                    profile.save()                    
            return redirect("index")
        else:
            return redirect("login")
    else:
        form = userSettingsForm()
        return render(request, 'settings.html', {"form":form})

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
            request.session['user'] = str(User.objects.get(email=e_mail).userid)
            return redirect("registerProfile")
    context = {'form': form}
    return render(request, 'register.html', context)