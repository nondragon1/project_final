from django.urls import path
from mealmaster.pages.Goal.views import goal , detailgoal , detailgoalfat , aftergoal , addExercise , addGoal , deleteGoal , ChangeGoal

urls = [
    path('goal/' , goal , name="goal"),
    path('goal/detailgoal/<int:id_diet>/' , detailgoal , name="detailgoal"),
    path('detailgoalfat/<int:id_diet>/', detailgoalfat , name="detailgoalfat"),
    path('aftergoal/', aftergoal , name="aftergoal"),

    path('goal/exercise/add', addExercise , name="addexercise"),

    path('goal/diet/<int:id_diet>/<str:jpeg_body>', addGoal , name="addgoal"),
    path('goal/delete/', deleteGoal , name="deletegoal"),
    path('goal/change/', ChangeGoal , name="changegoal"),
]

# /<int:id_image>/