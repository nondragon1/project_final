from django.shortcuts import render , redirect
from mealmaster.models import customer , Diet
import sweetify
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout

from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse
import random , time , asyncio

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
        print(user)
        if user :
            # print(user.is_authenticated)
            login(request, user)
            sweetify.success(request, 'Success \(>_<)/', timer=3000)
            return redirect('/')
        else:
            sweetify.error(request, 'Account not found', timer=3000)
            return redirect('/login')
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
            diet=None, 
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

def check_mail(request):
    if request.POST :
        email = request.POST.get("email")
        try :
            userData = customer.objects.get(email=email)
            return JsonResponse(
                data={
                    "user" : userData.username,
                    "fullname" : userData.name,
                    "image" : userData.image.url if userData.image else ""
                },
                status=200
            )
        except Exception as err :
            return JsonResponse(
                data={
                    "user" : "",
                    "fullname" : "",
                    "image" : ""
                },
                status=200
            )
    else :
        return render(request , "auth/forget/check_mail.html")

reset_codes = {}
def change_password(request):
    if request.POST :
        user_search = request.POST.get("user_search")
        reset_code = request.POST.get("verify_reset_code")
        
        new_password = request.POST.get("new-password")
        if user_search :
            userData = customer.objects.get(username=user_search)
            asyncio.run(send_reset_pass(userData.email))
            return render(request , "auth/forget/change_password.html" , {
                "user" : user_search
            })
        if reset_code :
            user = request.POST.get("user")
            userData = customer.objects.get(username=user)
            if reset_codes[userData.email] == reset_code :
                return JsonResponse(
                    data={},
                    status=200
                )
            else :
                return JsonResponse(
                    data={},
                    status=400
                )
        if new_password :
            user = request.POST.get("user")
            try :
                userData = customer.objects.get(username=user)
                userData.user.set_password(new_password)
                userData.user.save()
                userData.password = new_password
                userData.save()
                sweetify.success(request, 'Success reset password', timer=3000)
                return redirect('/login')
            except :
                sweetify.error(request, 'Fail reset password', timer=3000)
                return redirect('/login')
    else :
        return render(request , "auth/forget/change_password.html")

async def timeout_code(mail) :
    await asyncio.sleep(60 * 2)
    del reset_codes[mail]

def generate_verification_code():
    return str(random.randint(100000, 999999))

async def send_reset_pass(email : str):
    subject = 'Reset Code!'
    code = generate_verification_code()
    message = f'code : {code}.'
    email_from = f'Mealmaster <{settings.EMAIL_HOST_USER}>'
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list)

    reset_codes[email] = code
    asyncio.create_task(timeout_code(email))