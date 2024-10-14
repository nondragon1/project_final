from django import forms 
from .models import person  

class personForm(forms.ModelForm):
    class Meta: 
        model = person 
        fields = [
            'name',
            'weight',
            'height',
            'age',
            'gender',  
            'email', 
            'username', 
            'password',
            'phone',
            'cost',
            'image',
        ]