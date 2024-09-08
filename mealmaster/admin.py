from django.contrib import admin
from mealmaster.models import person

# Register your models here.
@admin.register(person)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("user", "name")