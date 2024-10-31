from django.shortcuts import render
from mealmaster.models import customer
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash

import sweetify
def profile(request):
    return render(request,"profile/profile.html")

def profile_password(request):
    if request.POST :
        userID = request.user.id
        curr_password = request.POST.get("current-password")
        new_password = request.POST.get("new-password")

        try :
            userData = customer.objects.get(user_id=userID)
            if curr_password == userData.password :
                userData.password = new_password
                userData.save()
                userData.user.set_password(new_password)
                userData.user.save()
                update_session_auth_hash(request, userData.user)
                sweetify.success(request, 'Success change password', timer=3000)
                return redirect(f"/profile")
            else :
                sweetify.error(request, 'Password incorrect', timer=3000)
                return redirect(f"/profile/password")
        except :
            sweetify.error(request, 'Fail change password', timer=3000)
            return redirect(f"/profile/password")

    return render(request,"profile/profile_password.html")

def profile_change_img(request):
    if request.POST :
        new_image = request.FILES.get("new_image")
        userID = request.user.id
        userData = customer.objects.get(user_id=userID)
        try :
            if new_image and userData.username :
                if userData.image:
                    userData.image.delete(save=False)
                userData.image = new_image
                userData.save()
        except :
            pass

    return JsonResponse(data={"result" : "update"} , status=200)

def upgrade(request):
    if request.POST :
        user_id = request.user.id
        user_data = customer.objects.get(user_id=user_id)
        if user_data.cost == "Normal" :
            user_data.cost = "Gold"
            user_data.save()
            sweetify.success(request, 'Success you Upgrade user', timer=3000)
            return redirect(f"/")

    return render(request,"profile/upgrade.html")