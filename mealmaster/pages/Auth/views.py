from django.shortcuts import render , redirect
from mealmaster.models import customer , Diet
# from .forms import personForm
from django.contrib import messages
import sweetify
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout

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
    return render(request,"auth/login.html")

def logout_user (request):
    logout(request)
    sweetify.success(request, 'Logged out successfully!', timer=3000)
    return redirect('/')

def register(request):
    # Check the incoming request
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        
        name=request.POST.get('name') 
        weight=request.POST.get('weight') 
        height=request.POST.get('height') 
        age=request.POST.get('age') 
        gender=request.POST.get('gender') 
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        image=request.FILES.get('image')
        diet=request.POST.get('diet') 
        cost=request.POST.get('cost') 
        # check user ซ้ำ

        person_obj = customer(
            user=user, 
            name=name, 
            weight=weight, 
            height=height, 
            age=age, 
            gender=gender, 
            email=email,
            username=username,
            password=password,
            phone=phone,
            image=image,
            diet=diet, 
            cost=cost, 
        )
        # personForm()
        person_obj.save()
        # form = personForm(request.POST, request.FILES)
        # form.save()
    
        return redirect("/login")

    diets_list = []
    diets = Diet.objects.values_list("id" , "name")
    
    for id_diet , diet_name in diets :
        diets_list.append({
            "value" : id_diet,
            "name" : diet_name 
        })

    return render(request,"auth/register.html", {
        "diet_list" : diets_list
    })