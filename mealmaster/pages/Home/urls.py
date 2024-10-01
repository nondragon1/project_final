from django.urls import path
from mealmaster.pages.Home.views import index , detailfood , goal , feed

urls = [
    path('', index),
    path('detailfood/<int:id_image>/', detailfood , name="detailfood"),

    path('goal/',goal, name="goal"),
    path('feed/',feed, name="feed"),
]