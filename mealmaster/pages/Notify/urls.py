from django.urls import path
from mealmaster.pages.Notify.views import update_notify

urls = [
    path('update-notify/',update_notify , name="profile"),
]