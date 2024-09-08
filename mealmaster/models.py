from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=4, blank=True)
    height = models.CharField(max_length=4, blank=True)
    age = models.CharField(max_length=4, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    cost = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="AppImages",blank=True)
    # image = forms.ImageField(upload_to="ProfileImages",blank=True)
    

    def __str__(self):
        return self.name