from django.urls import path
from mealmaster import views
from .views import register , feed , goal , diary , profile , upgrade , login_user , logout_user

urlpatterns = [
    path('', views.index),
    path('login/',login_user , name='login'),
    path('logout/',logout_user, name='logout'),
    path('register/',register ,name='register'),
    path('goal/',goal, name="goal"),
    path('diary/',diary, name="diary"),
    path('feed/',feed, name="feed"),
    path('profile/',profile , name="profile"),
    path('upgrade/',upgrade, name="upgrade"),
]