from django import forms
from .models import personchange  
from django.contrib.auth.models import User

class personchangeForm(forms.ModelForm):
    class Meta:
        model = personchange
        fields = ['cost']
