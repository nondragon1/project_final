from django.urls import path
from Goal import views
from .views import detailgoal , detailgoalfat , aftergoal

urlpatterns = [
    path('detailgoal/', detailgoal , name="detailgoal"),
    path('detailgoalfat/', detailgoalfat , name="detailgoalfat"),
    path('aftergoal/', aftergoal , name="aftergoal"),
] 