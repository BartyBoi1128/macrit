import datetime
from recipes.forms import UserCreationForm, registerProfileForm, userSettingsForm
from django.shortcuts import redirect, render
from django.template import loader
from recipes.models import User, Profile, Recipe, Diary, Food, Nutrition
import recipes.utils.nutrition as nuts
from recipes.service import *
from recipes.usersettings import *
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import recipes.warning_factory as warning_factory

# Create your views here.

def index(request):
    if 'user' in request.session:
        #Creates an instance of user
        user = request.session['user']
    return render(request, 'index.html', {})


def settings(request):
    return render(request, 'index.html', {})


@csrf_exempt
def login(request):
    form = UserCreationForm
    verify = 0
    if request.method == "POST":
        #Checks if the email is valid or used already 
        form = UserCreationForm(request.POST)
        for user in User.objects.all():
            #Check if the email and password are the same as the db
            if user.email == request.POST.get('email'):
                if user.password == request.POST.get('password1'):
                    request.session['user'] = user.userid
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
    user = User.objects.get(userid=request.session['user'])
    profile = Profile.objects.get(user=user)
    diary = Diary.objects.get(profile=profile)
    
    #Adding a recipe to the diary if the add button is clicked
    if request.method == "POST":
        recipe_name = request.POST.get('name')
        recipe = Recipe.objects.get(name=recipe_name)
        diary.intake.add(recipe)
    
    recipe_list = Recipe.objects.all()
    macro_dict = nuts.dict_decorator(nuts.generate_dict, diary, diary.nutrition)(nuts.generate_dict)
    warning_dict = dict()
    
    #Checking to see if the user has broken any food limits 
    for recipe in recipe_list:
        if warning_factory.buildWarning(recipe,macro_dict, profile) != -1:
            warning_dict[recipe.name] = warning_factory.buildWarning(recipe,macro_dict,profile).warningMessage().replace(" ","\u00a0")
        else:
            warning_dict[recipe.name] = warning_factory.buildWarning(recipe,macro_dict,profile)
    print(warning_dict)
    return render(request, 'recipe.html', {'recipe_list': recipe_list, 'warning_dict': warning_dict})

#Settings page for changing a user's macros
def settings(request):
    if request.method == "POST":
        
        #Creation of form for changing a user's macros
        form = userSettingsForm(request.POST) 
        
        #Creation of usersettings subject for observer design pattern
        
        #Creation of usersettings subject for observer design pattern
        current_settings = usersettings() 
        
        #Getting the currently logged in user
        user = User.objects.get(userid=request.session['user']) 
        
        if form.is_valid():
            #Populating of user's macros from the form
            pa = form.cleaned_data["profile_age"]
            pg = form.cleaned_data["profile_gender"]
            pw = form.cleaned_data["profile_weight"]
            ph = form.cleaned_data["profile_height"]
            pwg = form.cleaned_data["profile_weight_goal"]
            pwgt = form.cleaned_data["profile_weight_goal_time"]
            t = form.cleaned_data["profile_tags"]
            
            #Get the profile of the currently logged in user
            profile = Profile.objects.get(user=user) 
            
            #Get the Diary of the user's profile
            diary = Diary.objects.get(profile=profile) 
            
            #If any of the fields in the form are not null, change them
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
            if t == None:
                t = profile.tags
                
            #Set our subject's variables from the form
            current_settings.setAll(pa, pg, pw, ph, pwg, pwgt,t) 
            
            #Attach our nutrition observer to the subject
            current_settings.attach(diary.nutrition) 
            
            #Attach our profile observer to the subject
            current_settings.attach(profile) 
            
            #Notify both our observers
            current_settings.notify() 
            profile.save() 
            diary.nutrition.save()
            
            #Return to the index page once finished
            return redirect("index")
        else:
            return redirect("login")
    else:
        form = userSettingsForm()
        return render(request, 'settings.html', {"form": form})


def registerProfile(request):
    if request.method == "POST":
        form = registerProfileForm(request.POST)
        if form.is_valid():
            
            #Populating the users details from the entries
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
            t = form.cleaned_data["tags"]
            
            #Getting the current user and creating a profile with the inputted details
            current_user = User.objects.get(userid=request.session['user'])
            profile = Profile.objects.create(first_name=fn, second_name=sn, height=h, weight=w, BMI=bmiCalc(
                h, w), age=a, gender=g, weight_goal=wg, weight_goal_time=wgt, vegeterian=vgt, vegan=vg, user=current_user, tags=t)
            # cls, age, gender, weight, height, weightGoal, weightGoalTime, BMI):
            maintenance_calories = nuts.get_maintenance_calories(g, h, w, a)

            #Performing some simple calculations
            needed_fat = nuts.needed_fat(maintenance_calories)
            needed_saturates = nuts.needed_saturates(maintenance_calories)
            needed_sugar = nuts.needed_sugar(maintenance_calories)
            needed_protein = nuts.needed_protein(w)
            needed_carbs = nuts.needed_carbs(maintenance_calories)
            needed_fibre = nuts.needed_fibre(maintenance_calories)
            nutrition = Nutrition.objects.create(maintenance_calories=maintenance_calories, needed_fat=needed_fat, needed_saturates=needed_saturates, needed_sugar=needed_sugar, needed_protein=needed_protein, needed_carbs=needed_carbs, needed_fibre=needed_fibre, needed_salt=6)
            
            #Creating a diary with the gathered information
            Diary.objects.create(profile=profile, nutrition=nutrition)
            return redirect("login")
    else:
        form=registerProfileForm()
        return render(request, 'registerProfile.html', {"form": form})

@ csrf_exempt
def diary(request):
    if 'user' in request.session:
        
        #Getting the current user, profile, diary and nutrition info to display
        userid=request.session['user']
        user=User.objects.get(userid=userid)
        profile=Profile.objects.get(user=user)
        diary=Diary.objects.get(profile=profile)
        nutrition_info=nuts.dict_decorator(nuts.generate_dict, diary, diary.nutrition)(nuts.generate_dict)
        print(nutrition_info)
        data={'intake': diary.intake.all(),
            'nutrition_info': nutrition_info}
    return render(request, 'diary.html', data)

@ csrf_exempt
def register(request):
    form=UserCreationForm

    # cookies = {'csrftoken'}
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            #Gets email and password from the form and creates a user
            e_mail=request.POST.get('email', '')
            password=request.POST.get('password1')
            User.objects.create(email=e_mail, password=password)
            request.session['user']=User.objects.get(email=e_mail).userid
            return redirect("registerProfile")
    context={'form': form}
    return render(request, 'register.html', context)
    