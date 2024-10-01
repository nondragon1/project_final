from mealmaster.models import customer , Diet , Menus
from django.shortcuts import render , redirect

def index (request):
    if request.user.is_authenticated :
        id = request.user.id
        profile = customer.objects.filter(user_id=id).values("diet")
        diet_menu = Diet.objects.filter(id=profile[0].get("diet")).values("menu")
        menus = diet_menu[0].get("menu")
        menus_recommend = []
        for menu_id in menus :
            menu = Menus.objects.filter(id=menu_id).values("name" , "url_resource")
            menus_recommend.append({
                "value" : menu_id,
                "name" : menu[0].get("name"),
                "url" : menu[0].get("url_resource")
            })
        
        return render(request,"home/index.html" , {
            "menus" : menus_recommend
        })
        
    return render(request,"home/index.html")

def detailfood(request , id_image):
    menu_data = Menus.objects.filter(id=id_image).values("url_image")
    return render(request,"home/detailfood.html" , {
        "url_image" : menu_data[0].get("url_image")
    })

def views(request):
    return render(request,"home/home.html")

def goal(request):
    return render(request,"goal/goal1.html")

def feed(request):
    return render(request,"feed/feed.html")
