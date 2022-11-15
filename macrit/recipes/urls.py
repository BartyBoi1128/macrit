from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('recipe', views.recipes, name='recipe'),
    path('diary', views.diary, name='diary'),
]
