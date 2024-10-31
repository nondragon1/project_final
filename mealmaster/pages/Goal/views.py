from mealmaster.models import Diet , customer , FoodCalorie , DietUser , Menus , ExerciseCalorie , ImageBody
from django.shortcuts import render , redirect
from django.db import connection
import sweetify

from datetime import timedelta , datetime , timezone

def CalculateBMR(gender : str , weight : int , height : int , age : int) :
    if gender == "Male" :
        return 1.2 * (66 + (13.7 * weight) + (5 * height) - (6.8 * age))
    elif gender == "Female" :
        return 1.2 * (665 + (9.6 * weight) + (1.8 * height) - (4.7 * age))

def goal(request):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    if user_data.diet :
        return redirect("/aftergoal")
    else :
        diet_menus = Diet.objects.values("id" , "name")
        return render(request , "goal/goal1.html" , {
            "diet_menus" : diet_menus
        })

def detailgoal(request , id_diet):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    if user_data.diet :
        return redirect("/aftergoal")
    else :
        return render(request, f"goal/goals/goal{id_diet}.html" , {
            "id_diet" : id_diet
        })

def detailgoalfat(request , id_diet):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    if user_data.diet :
        return redirect("/aftergoal")
    else :
        return render(request,"goal/goal3.html" , {
            "id_diet" : id_diet,
            "gender" : "men" if user_data.gender == "Male" else "women"
        })

def aftergoal(request):
    user_id = request.user.id
    user_data = customer.objects.get(user_id=user_id)
    gender = user_data.gender
    weight = user_data.weight
    height = user_data.height
    age = user_data.age

    date_selected = request.GET.get("date")
    day_selected_query = None
    day_selected_template = ""
    if not date_selected == None :
        day_selected_convert = datetime.fromtimestamp(float(date_selected)) + timedelta(hours=7)
        day_selected_query = day_selected_convert.strftime('%Y-%m-%d %H:%M:%S')
        day_selected_template = day_selected_convert.strftime('%Y-%m-%d') 

    user_bmr = int(CalculateBMR(gender , weight , height , age))

    with connection.cursor() as cursor :
        select_date = (
            """
                CASE 
                    WHEN 
                        DATE(DATE_ADD(f.datetime, INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW(), INTERVAL 7 HOUR))
                        THEN 'TODAY'
                    WHEN 
                        DATE(DATE_ADD(f.datetime, INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW(), INTERVAL 7 HOUR)) - INTERVAL 1 DAY 
                        THEN 'YESTERDAY'
                    ELSE 'Other'
                END AS day
            """ if day_selected_query == None else
            """
                "DATE_SELECTED" AS day
            """
        )

        where_date = (
            """
                AND DATE(DATE_ADD(f.datetime, INTERVAL 7 HOUR)) = DATE(%(date_selected)s)
            """ if not day_selected_query == None else 
            ""
        )
        cursor.execute(f"""
            SELECT m.name , DATE_ADD(f.datetime , INTERVAL 7 HOUR) , m.calorie * f.rate_eat , {select_date}
            FROM {DietUser._meta.db_table} du 
            LEFT JOIN {FoodCalorie._meta.db_table} f ON du.id = f.diet_round_id
            LEFT JOIN {Menus._meta.db_table} m ON m.id = f.menu_id
            WHERE du.id = %(diet_round_id)s AND f.id {where_date}
        """ , {
            "diet_round_id" : user_data.diet,
            "date_selected" : day_selected_query
        })

        food_query = cursor.fetchall()
    
    with connection.cursor() as cursor :
        select_date = (
            """
                CASE 
                    WHEN 
                        DATE(DATE_ADD(exer.datetime, INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW(), INTERVAL 7 HOUR))
                        THEN 'TODAY'
                    WHEN 
                        DATE(DATE_ADD(exer.datetime, INTERVAL 7 HOUR)) = DATE(DATE_ADD(NOW(), INTERVAL 7 HOUR)) - INTERVAL 1 DAY 
                        THEN 'YESTERDAY'
                    ELSE 'Other'
                END AS day
            """ if day_selected_query == None else
            """
                "DATE_SELECTED" AS day
            """
        )

        where_date = (
            """
                AND DATE(DATE_ADD(exer.datetime, INTERVAL 7 HOUR)) = DATE(%(date_selected)s)
            """ if not day_selected_query == None else 
            ""
        )
        
        cursor.execute(f"""
            SELECT DATE_ADD(exer.datetime , INTERVAL 7 HOUR) , exer.calorie , {select_date}
            FROM {DietUser._meta.db_table} du 
            LEFT JOIN {ExerciseCalorie._meta.db_table} exer ON du.id = exer.diet_round_id
            WHERE du.id = %(diet_round_id)s AND exer.id {where_date}
        """ , {
            "diet_round_id" : user_data.diet,
            "date_selected" : day_selected_query
        })

        exercise_query = cursor.fetchall()

    food_calorie = []
    totals_food = {
        "today" : 0,
        "yesterday" : 0,
        "Days" : 0,
        "date_select" : 0
    }

    for food in food_query :
        calorie = int(food[2])
        food_calorie.append({
            "name" : food[0],
            "datetime" : food[1],
            "calorie" : calorie,
            "day" : food[3]
        })
        if food[3] == "TODAY" :
            totals_food["today"] += calorie
        if food[3] == "YESTERDAY" :
            totals_food["yesterday"] += calorie
        if food[3] == "DATE_SELECTED" :
            totals_food["date_select"] += calorie

        totals_food["Days"] += calorie
    
    exercise_calorie = []
    totals_exercise = {
        "today" : 0,
        "yesterday" : 0,
        "Days" : 0,
        "date_select" : 0
    }

    for exercise in exercise_query :
        calorie = int(exercise[1])
        exercise_calorie.append({
            "datetime" : exercise[0],
            "calorie" : calorie,
            "day" : exercise[2]
        })
        if exercise[2] == "TODAY" :
            totals_exercise["today"] += calorie
        if exercise[2] == "YESTERDAY" :
            totals_exercise["yesterday"] += calorie
        if exercise[2] == "DATE_SELECTED" :
            totals_exercise["date_select"] += calorie

        totals_exercise["Days"] += calorie
    
    diet_round = DietUser.objects.get(id=user_data.diet)

    day_start = diet_round.datetime_start
    day_now = datetime.now(timezone.utc) 
    day_diff = ((day_now + timedelta(hours=7)) - (day_start + timedelta(hours=7))).days
    
    diet_data = Diet.objects.get(id=diet_round.diet_id)

    bmr_days = user_bmr * (day_diff + 1 if day_diff == 0 else day_diff if day_diff <= 30 else 30)

    data_slides = [
        {
            "title" : "YESTERDAY",
            "id_element" : "ChartYesterday",
            "bmr" : user_bmr,
            "food" : totals_food["yesterday"],
            "exercise" : totals_exercise["yesterday"],
            "remain" : user_bmr - ( totals_food["yesterday"] + totals_exercise["yesterday"] if diet_data.id != 7 else totals_food["yesterday"] - totals_exercise["yesterday"] ),
        },
        {
            "title" : "TODAY",
            "id_element" : "ChartToDay",
            "bmr" : user_bmr,
            "food" : totals_food["today"],
            "exercise" : totals_exercise["today"],
            "remain" : user_bmr - ( totals_food["today"] + totals_exercise["today"] if diet_data.id != 7 else totals_food["today"] - totals_exercise["today"] ),
        }, 
        {
            "title" : "ALL 30 DAY",
            "id_element" : "ChartDays",
            "bmr" : bmr_days,
            "food" : totals_food["Days"],
            "exercise" : totals_exercise["Days"],
            "remain" : bmr_days - ( totals_food["Days"] + totals_exercise["Days"] if diet_data.id != 7 else totals_food["Days"] - totals_exercise["Days"] )
        }
    ] if not day_selected_template else [
        {
            "title" : day_selected_template,
            "id_element" : "TODAY",
            "bmr" : user_bmr,
            "food" : totals_food["date_select"],
            "exercise" : totals_exercise["date_select"],
            "remain" : user_bmr - ( totals_food["date_select"] + totals_exercise["date_select"] if diet_data.id != 7 else totals_food["date_select"] - totals_exercise["date_select"] ),
        }
    ]
    return render(request,"goal/aftergoal.html" , {
        "data_slides" : data_slides,
        "day_start" : day_start,
        "day_now" : day_now,
        "day_goal" : day_diff,
        "diet_type" : diet_data.name,
        "diet_body" : f"{diet_round.body}.jpg",
        "gender" : "men" if user_data.gender == "Male" else "women"
    })

def addExercise(request) :
    if request.method == "POST":
        if request.POST.get('submit-exercise') :
            try :
                user_id = request.user.id
                user_data = customer.objects.get(user_id=user_id)
            except :
                sweetify.success(request, 'ไม่พบผู้ใช้งาน!', timer=3000)
                return redirect(f"/aftergoal")

            diet_round_id = user_data.diet
            if diet_round_id :
                exercise_calorie = request.POST.get('add-exercise')
                exercise_time = request.POST.get('add-time')
                exercise = ExerciseCalorie(
                    diet_round_id = diet_round_id,
                    user_id = user_id,
                    calorie = exercise_calorie,
                    time_exercise = exercise_time
                )

                exercise.save()
                sweetify.success(request, 'ออกกำลังกายแล้ว!', timer=3000)
                return redirect(f"/aftergoal")
            else :
                sweetify.success(request, 'กรุณาเลือกการ Diet!', timer=3000)
                return redirect(f"/aftergoal")
        else :
            return redirect(f"/aftergoal")
    else :
        return redirect(f"/aftergoal")

def addGoal(request , id_diet , jpeg_body) :
    # เพิ่มรูป และ เวลา
    id = request.user.id
    try :
        profile = customer.objects.get(user_id=id)
    except :
        sweetify.success(request, 'ไม่พบผู้ใช้!', timer=3000)
        return redirect("/login")
    
    diet_round_id = profile.diet
    if not bool(diet_round_id) :
        diet_round = DietUser(
            diet_id=id_diet,
            body=jpeg_body
        )
        diet_round.save()

        profile.diet = diet_round.id
        profile.save()
        sweetify.success(request, 'เลือก Diet เรียบร้อย!', timer=3000)
        return redirect(f"/aftergoal")
    else :
        sweetify.success(request, 'โปรดยกเลิก Diet!', timer=3000)
        return redirect(f"/detailgoalfat/{id_diet}/")

def deleteGoal(request) :
    id = request.user.id
    try :
        profile = customer.objects.get(user_id=id)
    except :
        sweetify.success(request, 'ไม่พบผู้ใช้!', timer=3000)
        return redirect("/login")

    diet_round_id = profile.diet
    if diet_round_id :
        diet_round = DietUser.objects.get(id=diet_round_id)
        day_diff = ((datetime.now(timezone.utc) + timedelta(hours=7)) - (diet_round.datetime_start + timedelta(hours=7))).days

        if day_diff < 30 :
            diet_round.delete()
            # FoodCalorie.objects.filter(diet_round_id=diet_round_id).delete()
            # ExerciseCalorie.objects.filter(diet_round_id=diet_round_id).delete()
            
            profile.diet = None
            profile.save()
            sweetify.success(request, 'ยกเลิก Diet!', timer=3000)
            return redirect("/goal")
        else :
            sweetify.success(request, 'ล้มเหลวยกเลิก Diet!', timer=3000)
            return redirect("/aftergoal")
    else :
        sweetify.success(request, 'โปรดเลือก Diet!', timer=3000)
        return redirect("/goal")

def ChangeGoal(request) :
    id = request.user.id
    try :
        profile = customer.objects.get(user_id=id)
    except :
        sweetify.success(request, 'ไม่พบผู้ใช้!', timer=3000)
        return redirect("/login")

    diet_round_id = profile.diet
    if diet_round_id :
        diet_round = DietUser.objects.get(id=diet_round_id)
        day_diff = ((datetime.now(timezone.utc) + timedelta(hours=7)) - (diet_round.datetime_start + timedelta(hours=7))).days

        if day_diff >= 30 :

            user_id = request.user.id
            image_user = ImageBody(
                diet_round_id = diet_round_id,
                user_id = user_id,
                url_image = request.FILES.get('image-progress'),
            )

            image_user.save()

            profile.diet = None
            profile.save()
            sweetify.success(request, 'Success Diet!', timer=3000)
            return redirect("/goal")
        else :
            sweetify.success(request, 'ล้มเหลวเปลี่ยน Diet!', timer=3000)
            return redirect("/aftergoal")
    else :
        sweetify.success(request, 'โปรดเลือก Diet!', timer=3000)
        return redirect("/goal")