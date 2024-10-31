from django.contrib import admin
from mealmaster.models import customer , FoodCalorie

@admin.register(customer)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'username', 'password', 'email', 'name',
        'weight', 'height', 'age', 'gender', 'phone', 'image', 'cost'
    )

@admin.register(FoodCalorie)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'image_upload' , 'datetime'
    )