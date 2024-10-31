from django.urls import path
from mealmaster.pages.Auth.views import login_user , logout_user , register , check_mail , change_password

urls = [
    path('login/', login_user , name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register , name='register'),
    path('forget/', check_mail , name='forget'),
    path('forget/change', change_password , name='forget_change'),
]