from django.contrib import admin
from mealmaster.models import adminModel

# Register your models here.
@admin.register(adminModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("user", "name")