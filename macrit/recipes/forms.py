from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import User as wagwan
from django.core.exceptions import ValidationError

#self.profile_age, self.profile_gender, self.profile_weight,self.profile_height,self.profile_weight_goal,self.profile_weight_goal_time, self.profile_bmi
class userSettingsForm(forms.Form):
    profile_age = forms.FloatField(label= "Age", required=False)
    profile_gender = forms.BooleanField(label= "ChangeGender?", required=False)
    profile_weight = forms.FloatField(label= "Weight", required=False)
    profile_height = forms.FloatField(label= "Height", required=False)
    profile_weight_goal = forms.FloatField(label= "Weight Goal", required=False)
    profile_weight_goal_time = forms.DateField(label= "Weight Goal Time", required=False)
    profile_tags = forms.CharField(label= "Allergies/HealthConditions", required=False)

class registerProfileForm(forms.Form):
    first_name = forms.CharField(label = "First Name", max_length=50)
    second_name = forms.CharField(label = "Second Name", max_length=100)
    height = forms.FloatField(label= "Height")
    weight = forms.FloatField(label= "Weight")
    age = forms.FloatField(label= "Age")
    gender = forms.BooleanField(label= "Male?", required=False)
    weight_goal = forms.FloatField(label = "Weight Goal")
    weight_goal_time = forms.DateField(label = "Weight Goal Date")
    vegeterian = forms.BooleanField(label= "Are you vegeterian?", required=False)
    vegan = forms.BooleanField(label= "Are you vegan?", required=False)
    tags = forms.CharField(label = "Allergies/HealthConditions", required=False)

class UserCreationForm(UserCreationForm):
    def validate_email(value):
        for user in wagwan.objects.all():
                if user.email == value:
                    raise ValidationError("Email already exists")

    email = forms.EmailField(required=True, validators=[validate_email])

    class Meta: 
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user