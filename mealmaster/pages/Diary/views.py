from mealmaster.models import ImageBody , FoodCalorie , Menus
from django.shortcuts import render , redirect
from django.db import connection
import sweetify
from django.http import JsonResponse

from datetime import datetime , timedelta , timezone

def diary(request):
    user_id = request.user.id
    # Images_progress = ImageBody.objects.filter(user_id=user_id).values("url_image" , "datetime").order_by("datetime")
    
    with connection.cursor() as cursor :
        cursor.execute(f"""
            SELECT 
                f.id ,
                m.name , 
                -- DATE_ADD(f.datetime , INTERVAL 7 HOUR) , 
                TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) , 
                m.calorie * f.rate_eat
                -- CASE 
                --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '00:00:00' AND '11:59:59' THEN 'Breakfast'
                --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '12:00:00' AND '17:59:59' THEN 'Lunch'
                --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '18:00:00' AND '23:59:59' THEN 'Dinner'
                --     ELSE 'Unknown'
                -- END AS time_of_day
            FROM {FoodCalorie._meta.db_table} f
            LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
            WHERE user_id = %(user_id)s AND
                DATE_ADD(f.datetime , INTERVAL 7 HOUR) BETWEEN DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) AND DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) + INTERVAL 1 DAY - INTERVAL 1 SECOND
        """ , {
            "user_id" : user_id
        })

        food_calorie = []
        total = 0
        for food in cursor.fetchall() :
            food_calorie.append({
                "id" : food[0],
                "name" : food[1],
                # "datetime" : food[1],
                "time" : food[2].strftime("%H:%M"),
                "calorie" : food[3],
                # "time_of_day" : food[4]
            })
            total += int(food[3])
        
    days_history = []
    food_calorie_history = []
    day_selected = ""
    day_selected_template = ""
    if request.GET.get('date') :
        day_selected = request.GET.get('date')
        try :
            day_selected_convert = datetime.fromtimestamp(float(day_selected)) + timedelta(hours=7)
            day_selected_query = day_selected_convert.strftime('%Y-%m-%d %H:%M:%S')
            day_selected_template = day_selected_convert.strftime('%Y-%m-%d')
            with connection.cursor() as cursor :
                cursor.execute(f"""
                    SELECT m.name , 
                        -- DATE_ADD(f.datetime , INTERVAL 7 HOUR) , 
                        TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) , 
                        m.calorie * f.rate_eat
                        -- CASE 
                        --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '00:00:00' AND '11:59:59' THEN 'Breakfast'
                        --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '12:00:00' AND '17:59:59' THEN 'Lunch'
                        --     WHEN TIME(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) BETWEEN '18:00:00' AND '23:59:59' THEN 'Dinner'
                        --     ELSE 'Unknown'
                        -- END AS time_of_day
                    FROM {FoodCalorie._meta.db_table} f
                    LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
                    WHERE user_id = %(user_id)s AND
                        DATE_ADD(f.datetime , INTERVAL 7 HOUR) BETWEEN DATE(%(day_history)s) AND DATE(%(day_history)s) + INTERVAL 1 DAY - INTERVAL 1 SECOND
                """ , {
                    "user_id" : user_id,
                    "day_history" : day_selected_query
                })

                # (DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL %(day_history_count)s DAY ) AND (DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) + INTERVAL 1 DAY - INTERVAL 1 SECOND) + INTERVAL %(day_history_count)s DAY

                for food_history in cursor.fetchall() :
                    food_calorie_history.append({
                        "name" : food_history[0],
                        # "datetime" : food_history[1],
                        "time" : food_history[1].strftime("%H:%M"),
                        "calorie" : food_history[2],
                        # "time_of_day" : food_history[3]
                    })
        except Exception as err :
            pass

    for count_day in range(0 , 3) :
        day_history = datetime.now(timezone.utc) - timedelta(days=count_day) + timedelta(hours=7)
        days_history.append({
            "daystr" : day_history.strftime("%d %b %Y"),
            "datetime" : day_history.timestamp(),
            "selected" : day_history.strftime("%d/%m/%Y") == datetime.fromtimestamp(float(day_selected)).strftime("%d/%m/%Y") if day_selected else False
        })

    days_history.reverse()
    return render(request,"diary/diary.html" , {
        # "images" : Images_progress,
        "food_calorie" : food_calorie,
        "total" : total,
        "list_stage" : ["Breakfast", "Lunch", "Dinner"],
        "days_history" : {
            "days" : days_history,
            "foods_calorie" : food_calorie_history,
            "default" : day_selected_template
        }
    })

def delete_food(request) :
    if request.method == "POST" :
        user_id = request.user.id
        id_food = request.POST.get("id_food")

        food_eat = FoodCalorie.objects.get(id=id_food)

        if food_eat.user_id == user_id :
            food_eat.delete()
            return JsonResponse(
                data={},
                status=200
            )
        else :
            return JsonResponse(
                data={},
                status=400
            )

def add_progress(request):
    # if request.method == "POST" :
    #     user_id = request.user.id
    #     image_user = ImageBody(
    #         user_id = user_id,
    #         url_image = request.FILES.get('image-progress'),
    #     )

    #     image_user.save()
    #     sweetify.success(request, 'Save image success \(>_<)/', timer=3000)
    #     return redirect('/diary')
    
    return render(request,"diary/add_progress.html")
