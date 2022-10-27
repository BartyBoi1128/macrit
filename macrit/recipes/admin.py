from django.contrib import admin

from .models import User
from .models import Profile
from .models import Diary
from .models import Ingredient
from .models import ShoppingList
from .models import Recipe
from .models import Macro
from .models import HealthCondition

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Diary)
admin.site.register(Ingredient)
admin.site.register(ShoppingList)
admin.site.register(Recipe)