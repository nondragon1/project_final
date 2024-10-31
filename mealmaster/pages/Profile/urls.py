from django.urls import path
from mealmaster.pages.Profile.views import profile , profile_password , profile_change_img , upgrade

urls = [
    path('profile/',profile , name="profile"),
    path('profile/image',profile_change_img , name="profile_change"),
    path('profile/password',profile_password , name="profile_password"),
    path('upgrade/',upgrade, name="upgrade"),
]