from django.urls import path
from mealmaster import views
from mealmaster.pages.Home.urls import urls as urls_home
from mealmaster.pages.Auth.urls import urls as urls_auth
from mealmaster.pages.Profile.urls import urls as urls_profile
from mealmaster.pages.Diary.urls import urls as urls_diary
from mealmaster.pages.Predict.urls import urls as urls_predict

urlpatterns = [
    *urls_home,
    *urls_auth,
    *urls_profile,
    *urls_diary,
    *urls_predict
]