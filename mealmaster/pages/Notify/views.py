from django.shortcuts import render
from mealmaster.models import customer , FoodCalorie , Menus , Notify , ExerciseCalorie
from django.shortcuts import redirect
from django.db import connection
import sweetify
from django.http import JsonResponse
from mealmaster.pages.Goal.views import CalculateBMR

def update_status(request) :
    if request.POST :
        id_unread = request.POST.get("id_unread")
        for id in id_unread.split(",") :
            notify = Notify.objects.get(id=id)
            notify.status = True
            notify.save()

def update_notify(request):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    
    if user_data.diet :
        diet_round_id = user_data.diet
    
        with connection.cursor() as cursor_notify_check :
            cursor_notify_check.execute(f"""
                SELECT id
                FROM {Notify._meta.db_table} n
                WHERE n.user_id = %(user_id)s AND 
                    DATE_ADD(n.datetime , INTERVAL 7 HOUR) BETWEEN
                        DATE_ADD(NOW() , INTERVAL 7 HOUR) - INTERVAL 5 MINUTE
                            AND
                        DATE_ADD(NOW() , INTERVAL 7 HOUR)
            """ , {
                "user_id" : user_id
            })

            # 
            # DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 5 MINUTE
            #                 AND
            #             DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND

            if not len(cursor_notify_check.fetchall()) :
                with connection.cursor() as cursor_food :
                    cursor_food.execute(f"""
                        SELECT
                            (
                                SELECT SUM(m.calorie * f.rate_eat)
                                FROM {FoodCalorie._meta.db_table} f
                                LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
                                WHERE f.diet_round_id = u.diet AND DATE(DATE_ADD(f.datetime , INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR))
                            ) as sum_food,
                            (
                                SELECT calorie
                                FROM {ExerciseCalorie._meta.db_table} ex
                                WHERE ex.diet_round_id = u.diet AND DATE(DATE_ADD(ex.datetime , INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR))
                            ) as sum_exercise
                        FROM {customer._meta.db_table} u
                        WHERE u.diet IS NOT NULL AND u.user_id = %(user_id)s AND u.diet = %(diet_round_id)s
                    """ , {
                        "user_id" : user_id,
                        "diet_round_id" : diet_round_id
                    })

                    user_notify = cursor_food.fetchone()
                    calFood = user_notify[0] if user_notify[0] else 0
                    calExercise = user_notify[1] if user_notify[1] else 0
                    BMR = CalculateBMR(user_data.gender , user_data.weight , user_data.height , user_data.age)
                    Message = "Calorie Over" if BMR < (calFood + calExercise) else "Calorie less" if BMR > (calFood + calExercise) else ""

                    notify = Notify(
                        user_id = user_id,
                        msg = Message,
                    )

                    notify.save()

        notify_list = Notify.objects.filter(user_id=user_id).values("id", "datetime", "msg", "status").order_by('-datetime')[:5]
        count_unread = 0
        id_unread = []
        notify_data = []
        for noti in notify_list :
            if not noti["status"] :
                count_unread += 1
                id_unread.append(noti["id"])
            
            notify_data.append(noti)
            
        return JsonResponse(
            {
                "notify" : notify_data,
                "count" : count_unread,
                "id_unreads" : id_unread
            }
        )
    else :
        return JsonResponse(
            {
                "notify" : [],
                "count" : 0,
                "id_unreads" : []
            }
        )
            # 
            # f.datetime
            #                         BETWEEN 
            #                             DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
            #                                AND
            #                             DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND

            #
            # ex.datetime
            #                         BETWEEN
            #                             DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
            #                                 AND
            #                             DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND

            # DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
            #                             AND
            #                         DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND