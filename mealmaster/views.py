from django.shortcuts import render , redirect
from django.http import HttpResponse
from mealmaster.models import person
# from .forms import personForm
from django.contrib import messages
import sweetify
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout


# Create your views here.

#home

def index (request):
    return render(request,"frontend/index.html")


def login_user(request):
    if request.method == "POST":
        # print(request.POST)
        # import pdb; pdb.set_trace()
        # request.POST
        username = request.POST["username"]
        password = request.POST["password"]
        # user = User.objects.filter(username=username, password=password)
        # import pdb; pdb.set_trace()
        user = authenticate(username=username, password=password)
        if user :
            # print(user.is_authenticated)
            login(request, user)
            sweetify.success(request, 'Success \(>_<)/', timer=3000)
            return redirect('/')
        else:
            messages.info(request, "ID NOT FOUND!!!")
    return render(request,"frontend/login.html")

def logout_user (request):
    logout(request)
    sweetify.success(request, 'Logged out successfully!', timer=3000)
    return redirect('/')




def register(request):
    # Check the incoming request
    if request.method == "POST":
        # print(request.POST)
        # import pdb; pdb.set_trace()
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        person_obj = person(user=user, name=request.POST.get('name'), cost=request.POST.get('cost'), phone=request.POST.get('phone'), 
                            weight=request.POST.get('weight'), height=request.POST.get('height'), age=request.POST.get('age'), 
                            gender=request.POST.get('gender'), image=request.FILES.get('image'))
        # personForm()
        person_obj.save()
        # form = personForm(request.POST, request.FILES)
        # form.save()
    
        return redirect("/login")
    return render(request,"frontend/register.html", {})

def home(request):
    return render(request,"frontend/home.html")

def goal(request):
    return render(request,"frontend/goal1.html")

def diary(request):
    return render(request,"frontend/diary.html")

def feed(request):
    return render(request,"frontend/feed.html")


def profile(request):
    return render(request,"frontend/profile.html")

def upgrade(request):
    return render(request,"frontend/upgrade.html")