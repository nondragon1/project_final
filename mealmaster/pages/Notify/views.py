from django.shortcuts import render
from mealmaster.models import customer , FoodCalorie , Menus , Notify , ExerciseCalorie
from django.shortcuts import redirect
from django.db import connection
import sweetify

def update_notify(request):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    diet_round_id = user_data.diet
    
    
    with connection.cursor() as cursor_notify_check :
        cursor_notify_check.execute(f"""
            SELECT id
            FROM {Notify._meta.db_table} n
            WHERE n.user_id = %(user_id)s AND 
                n.datetime BETWEEN
                    DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 HOUR
                        AND
                    DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND
        """ , {
            "user_id" : user_id
        })

        if not len(cursor_notify_check.fetchall()) :
            with connection.cursor() as cursor_food :
                cursor_food.execute(f"""
                    SELECT u.user_id, u.age, u.weight, u.height, u.gender , 
                        (
                            SELECT SUM(m.calorie * f.rate_eat)
                            FROM {FoodCalorie._meta.db_table} f
                            LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
                            WHERE f.diet_round_id = u.diet AND 
                                f.datetime
                                    BETWEEN 
                                        DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
                                            AND
                                        DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND
                        ) as sum_food,
                        (
                            SELECT calorie
                            FROM {ExerciseCalorie._meta.db_table} ex
                            WHERE ex.diet_round_id = u.diet AND 
                                ex.datetime
                                    BETWEEN
                                        DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
                                            AND
                                        DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND
                        ) as sum_exercise
                    FROM {customer._meta.db_table} u
                    WHERE u.diet IS NOT NULL AND u.user_id = %(user_id)s AND u.diet_round_id = %(diet_round_id)s
                """ , {
                    "user_id" : user_id,
                    "diet_round_id" : diet_round_id
                })

                user_notify = cursor_food.fetchall()
                return {
                    "data" : user_notify
                }
            # DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 DAY
            #                             AND
            #                         DATE(DATE_ADD(NOW() , INTERVAL 7 HOUR)) - INTERVAL 1 SECOND