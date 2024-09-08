from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def detailfood(request):
    return render(request,"frontend/detailfood.html")