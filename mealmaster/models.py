from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class adminModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, blank=True)

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    image = models.ImageField(upload_to="AppImages",blank=True)
    cost = models.CharField(max_length=10 , blank=True)
    diet = models.IntegerField(blank=True)
    role = models.CharField(max_length=10, blank=True)
    # image = forms.ImageField(upload_to="ProfileImages",blank=True)
    def __str__(self):
        return self.name

class FoodCalorie(models.Model):
    user_id = models.IntegerField(blank=True)
    menu_id = models.IntegerField(blank=True)
    rate_eat = models.FloatField(default=0.0 , blank=True)
    datetime = models.DateTimeField(default=timezone.now)

class ImageBody(models.Model):
    user_id = models.IntegerField(blank=True)
    url_image = models.ImageField(upload_to="progress",blank=True)
    datetime = models.DateTimeField(default=timezone.now) 
    
class Diet(models.Model):
    name = models.CharField(max_length=50, blank=True)
    detail = models.TextField(blank=True)
    menu = models.JSONField(blank=True , default=list)
    url = models.TextField(blank=True)

class Menus(models.Model):
    name = models.CharField(max_length=50, blank=True)
    label = models.TextField(blank=True)
    calorie = models.IntegerField(blank=True)
    url_image = models.ImageField(upload_to="thaimenu",blank=True)
    url_resource = models.TextField(blank=True)
# class 