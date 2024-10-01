from django.shortcuts import render

def profile(request):
    return render(request,"profile/profile.html")

def upgrade(request):
    return render(request,"profile/upgrade.html")