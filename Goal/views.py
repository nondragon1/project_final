from django.shortcuts import render

# Create your views here.

def detailgoal(request):
    return render(request,"frontend/goal2.html")

def detailgoalfat(request):
    return render(request,"frontend/goal3.html")

def aftergoal(request):
    return render(request,"frontend/aftergoal.html")