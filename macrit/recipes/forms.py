from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import User as wagwan
from django.core.exceptions import ValidationError

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
