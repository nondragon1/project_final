from django.urls import path
from mealmaster.pages.Home.views import index , detailfood , detailfoodAdd , feed , category

urls = [
    path('', index),
    path('detailfood/<int:id_image>/', detailfood , name="detailfood"),
    path('detailfood/add/<int:menu_id>/', detailfoodAdd , name="detailfood"),

    path('category/<int:category_id>/', category , name="category"),

    path('feed/',feed, name="feed"),
]