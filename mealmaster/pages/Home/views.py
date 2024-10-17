from mealmaster.models import customer , Diet , Menus , DietUser , FoodCalorie , Category
from django.shortcuts import render , redirect
import sweetify

def index (request):
    if request.user.is_authenticated :
        id = request.user.id

        profile = customer.objects.get(user_id=id)
        if profile :
            try :
                diet_round = DietUser.objects.get(id=profile.diet)
                diet_menu = Diet.objects.get(id=diet_round.diet_id)
            except :
                diet_menu = None
            menus_recommend = []
            if diet_menu :
                menus = diet_menu.menu

                for menu_id in menus :
                    menu = Menus.objects.filter(id=menu_id).values("name" , "url_resource")
                    menus_recommend.append({
                        "value" : menu_id,
                        "name" : menu[0].get("name"),
                        "url" : menu[0].get("url_resource")
                    })
            
            categorys = Category.objects.values("id" , "name")

            return render(request,"home/index.html" , {
                "menus" : menus_recommend,
                "categorys" : categorys
            })
        else :
            sweetify.success(request, 'ไม่พบผู้ใช้', timer=3000)
            return redirect("/login")
        
    categorys = Category.objects.values("id" , "name")
    return render(request,"home/index.html" , {
        "categorys" : categorys
    })

def detailfood(request , id_image):
    menu_data = Menus.objects.filter(id=id_image).values("id" , "url_image" , "calorie")
    return render(request,"home/detailfood.html" , {
        "url_image" : menu_data[0].get("url_image"),
        "menu_id" : menu_data[0].get("id"),
        "calorie" : menu_data[0].get("calorie"),
    })

def detailfoodAdd(request) :
    if request.POST :
        user_id = request.user.id
        profile = customer.objects.get(user_id=user_id)
        menu_id = request.POST.get("menu_id")
        number = request.POST.get("number")

        if menu_id and number and user_id :
            try :
                diet_round_id = profile.diet
                if diet_round_id :
                    foodCalorie = FoodCalorie(
                        diet_round_id=diet_round_id,
                        user_id=user_id,
                        menu_id=menu_id,
                        rate_eat=number
                    )

                    foodCalorie.save()
                    sweetify.success(request, 'Eat !!', timer=3000)
                    return redirect(f"/")
                else :
                    sweetify.success(request, 'Please select Diet!', timer=3000)
                    return redirect(f"/")
            except :
                sweetify.success(request, 'No data !!', timer=3000)
                return redirect(f"/")

def views(request):
    return render(request,"home/home.html")

def feed(request):
    return render(request,"feed/feed.html")

def category(request , category_id) :
    category_data = Category.objects.get(id=category_id)

    menus = []
    for menu_id in category_data.menus :
        menu_data = Menus.objects.get(id=menu_id)
        menus.append({
            "value" : menu_id,
            "url" : menu_data.url_resource,
            "name" : menu_data.name
        })

    return render(request , "home/category.html" , {
        "title" : category_data.name,
        "menus" : menus
    })