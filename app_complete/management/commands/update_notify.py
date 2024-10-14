from django.core.management.base import BaseCommand
from mealmaster.models import Notify , FoodCalorie , customer , Menus
from datetime import datetime
from django.db import connection
from mealmaster.pages.Goal.views import CalculateBMR

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor :
            cursor.execute(f"""
                SELECT u.user_id, u.age, u.weight, u.height, u.gender , 
                    (
                        SELECT SUM(m.calorie * f.rate_eat)
                        FROM {FoodCalorie._meta.db_table} f
                        LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
                        WHERE f.diet_round_id = u.diet AND f.datetime BETWEEN DATE_ADD(NOW() , INTERVAL 7 HOUR) - INTERVAL 1 DAY 
                            AND DATE_ADD(NOW() , INTERVAL 7 HOUR) - INTERVAL 1 SECOND
                    ) as sum_food

                FROM {customer._meta.db_table} u
                WHERE u.diet IS NOT NULL
            """)
        
            for user_food_diary in cursor.fetchall() :
                user_id = user_food_diary[0]
                age = user_food_diary[1]
                weight = user_food_diary[2]
                height = user_food_diary[3]
                gender = user_food_diary[4]
                calall = user_food_diary[5]

                bmr = CalculateBMR(gender , weight , height , age)
                
                notify_user = Notify(
                    user_id = user_id,
                    msg = "Overeating" if bmr < calall else "Eat less than prescribed"
                )

                notify_user.save()
        
        self.stdout.write(f"Updated notify.")