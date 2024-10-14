from django.shortcuts import render
from mealmaster.models import customer
from django.shortcuts import redirect
import sweetify
def profile(request):
    return render(request,"profile/profile.html")

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