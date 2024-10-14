from django.urls import path
from Goal import views
from .views import detailgoalfat , aftergoal

urlpatterns = [
    path('detailgoalfat/', detailgoalfat , name="detailgoalfat"),
    path('aftergoal/', aftergoal , name="aftergoal"),
] 