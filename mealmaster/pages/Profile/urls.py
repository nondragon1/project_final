from django.urls import path
from mealmaster.pages.Profile.views import profile , upgrade

urls = [
    path('profile/',profile , name="profile"),
    path('upgrade/',upgrade, name="upgrade"),
]