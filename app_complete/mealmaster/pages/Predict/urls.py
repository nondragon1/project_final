from django.urls import path
from mealmaster.pages.Predict.views import Predict , PredictMenu , SelectMenu

urls = [
    path('predict/',Predict , name="predict"),
    path('predict/menu', PredictMenu , name="predict"),
    path('predict/select', SelectMenu , name="predict"),
]