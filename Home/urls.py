from django.urls import path
from mealmaster import views
from .views import detailfood

urlpatterns = [
    path('detailfood/',detailfood, name="detailfood"),

]