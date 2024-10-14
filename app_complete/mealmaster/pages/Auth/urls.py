from django.urls import path
from mealmaster.pages.Auth.views import login_user , logout_user , register 

urls = [
    path('login/', login_user , name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register , name='register'),
]