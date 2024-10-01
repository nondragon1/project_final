from django.urls import path
from mealmaster.pages.Diary.views import diary , add_progress

urls = [
    path('diary/',diary, name="diary"),
    path('diary/add_progress',add_progress, name="diary_add_progress"),
]