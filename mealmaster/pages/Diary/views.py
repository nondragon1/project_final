from mealmaster.models import ImageBody , FoodCalorie
from django.shortcuts import render , redirect
import sweetify

def diary(request):
    user_id = request.user.id
    Images_progress = ImageBody.objects.filter(user_id=user_id).values("url_image" , "datetime").order_by("datetime")
    # FoodCalory = FoodCalorie.objects.filter(user_id=user_id).values()
    
    return render(request,"diary/diary.html" , {
        "images" : Images_progress
    })

def add_progress(request):
    if request.method == "POST" :
        user_id = request.user.id
        image_user = ImageBody(
            user_id = user_id,
            url_image = request.FILES.get('image-progress'),
        )

        image_user.save()
        sweetify.success(request, 'Save image success \(>_<)/', timer=3000)
        return redirect('/diary')
    
    return render(request,"diary/add_progress.html")
