from django.urls import path
from mealmaster.pages.Notify.views import update_notify , update_status

urls = [
    path('update-notify/',update_notify , name="update_notify"),
    path('update-status/',update_status , name="update_status"),
]