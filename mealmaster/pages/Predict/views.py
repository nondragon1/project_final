from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import base64
from PIL import Image, UnidentifiedImageError
import numpy as np
import io , os
from pathlib import Path
from mealmaster.models import Menus , FoodCalorie , customer
from uuid import uuid4

from datetime import datetime , timezone , timedelta

from fastai.vision.all import (
    load_learner
)
# from keras.models import load_model
# from keras.layers import BatchNormalization

# โหลดโมเดล
# model_path = "/app/Flaskapi/ML_model40ep.h5"
model_path = "/app/mealmaster/modules/export.pkl"
model = load_learner(model_path, cpu=True)
# model = load_model('C:/Users/Admin/Desktop/ProjectEX/mealmasterApp/Flaskapi/ML_model40ep.h5', custom_objects={'BatchNormalization': BatchNormalization})
def preprocess_image(uploaded_file):
    try:
        img = Image.open(uploaded_file)
        
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        img = img.resize((224, 224))  # ปรับขนาดให้ตรงกับที่โมเดลต้องการ
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        return img_array
    except UnidentifiedImageError:
        return None

def fastai_process_image(uploaded_file) :
    image = Image.open(uploaded_file)

    if image.mode == 'RGBA':
        image = image.convert('RGB')

    id = uuid4()
    image_path = f"/app/mealmaster/pages/Predict/temp/{id}_temp_image.jpg"
    image.save(image_path)
    
    return image_path

# convert dict
thaimenu={
    "00":"แกงเขียวหวานไก่","01":"แกงเทโพ","02":"แกงเลียง","03":"แกงจืดเต้าหู้หมูสับ","04":"แกงจืดมะระยัดไส้",
    "05":"แกงมัสมั่นไก่","06":"แกงส้มกุ้ง","07":"ไก่ผัดเม็ดมะม่วงหิมพานต์","08":"ไข่เจียว","09":"ไข่ดาว",
    "10":"ไข่พะโล้","11":"ไข่ลูกเขย","12":"กล้วยบวชชี","13":"ก๋วยเตี๋ยวคั่วไก่","14":"กะหล่ำปลีผัดน้ำปลา",
    "15":"กุ้งแม่น้ำเผา","16":"กุ้งอบวุ้นเส้น","17":"ขนมครก","18":"ข้าวเหนียวมะม่วง","19":"ข้าวขาหมู",
    "20":"ข้าวคลุกกะปิ","21":"ข้าวซอยไก่","22":"ข้าวผัด","23":"ข้าวผัดกุ้ง","24":"ข้าวมันไก่",
    "25":"ข้าวหมกไก่","26":"ต้มข่าไก่","27":"ต้มยำกุ้ง","28":"ทอดมัน","29":"ปอเปี๊ยะทอด",
    "30":"ผักบุ้งไฟแดง","31":"ผัดไท","32":"ผัดกะเพรา","33":"ผัดซีอิ๊วเส้นใหญ่","34":"ผัดฟักทองใส่ไข่",
    "35":"ผัดมะเขือยาวหมูสับ","36":"ผัดหอยลาย","37":"ฝอยทอง","38":"พะแนงไก่","39":"ยำถั่วพู",
    "40":"ยำวุ้นเส้น","41":"ลาบหมู","42":"สังขยาฟักทอง","43":"สาคูไส้หมู","44":"ส้มตำ","45":"หมูปิ้ง","46":"หมูสะเต๊ะ","47":"ห่อหมก"
}

def Predict(request):
    return render(request,"predict/index.html")

def PredictMenu(request) :
    if request.method == 'POST':
        if 'image-progress' not in request.FILES:
            return JsonResponse({'error': 'No file part in the request'}, status=400)

        file = request.FILES['image-progress']

        if file.name == '':
            return JsonResponse({'error': 'No selected file'}, status=400)

        processed_image = fastai_process_image(file)

        if processed_image is None:
            return JsonResponse({'error': 'Cannot process the uploaded file as an image'}, status=400)

        try:
            predictions = model.predict(processed_image)
            os.remove(processed_image)
            # class_labels = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']           
            percent_verify = 65
            
            # top_max = 1
            # predicted_class_top = np.argsort()[-top_max:][::-1]
            
            # predicted_class = [class_labels[class_label] for class_label in predicted_class_top]
            predicted_class = [predictions[0]]
            # confidence = np.max(predictions) * 100
            confidence = predictions[2].tolist()[predictions[1].item()] * 100
             # Display the prediction
            # show = [thaimenu[predict] for predict in predicted_class]
            menu_selecteds= []
            if confidence > percent_verify :
                for menu in Menus.objects.filter(label__in=predicted_class).values("id" , "name" , "url_image" , "calorie") :
                    menu_selecteds.append(menu)
            
            return JsonResponse({"label" : predicted_class , "menus" : menu_selecteds , 'confidence': confidence})
        except Exception as e:
            print(e)
            return JsonResponse({'error': f'Prediction error: {str(e)}'}, status=500)

    return JsonResponse(
        data={
            "data" : 1
        }
    )

@api_view(['POST'])
def SelectMenu(request) :
    object_return = {
        "title" : "",
        "status" : "",
        "status_response" : 400
    }
    user_id = request.user.id
    menu_id = request.POST.get("menu_id")
    number = request.POST.get("number")

    profile = customer.objects.get(user_id=user_id)
    
    if menu_id and number and user_id :
        try :
            diet_round_id = profile.diet
            if diet_round_id :
                date_str = request.POST.get("date")
                time_str = request.POST.get("time")
                if time_str :
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() 
                    # (datetime.now(timezone.utc) + timedelta(hours=7)).date()
                    time_obj = datetime.strptime(time_str, "%H:%M").time()
                    combined_datetime = datetime.combine(date_obj, time_obj)
                    utc_datetime = combined_datetime - timedelta(hours=7)
                else :
                    utc_datetime = datetime.now(timezone.utc)

                foodCalorie = FoodCalorie(
                    diet_round_id=diet_round_id,
                    user_id=user_id,
                    menu_id=menu_id,
                    rate_eat=number,
                    datetime=utc_datetime,
                    image_upload=request.FILES.get('image-predict')
                )

                foodCalorie.save()
                object_return = {
                    "title" : "Eat \(>_<)/",
                    "status" : "success",
                    "status_response" : 200,
                }
            else :
                object_return = {
                    "title" : "Please select Diet",
                    "status" : "error",
                    "status_response" : 403,
                }
        except Exception as err :
            print(err)
            object_return = {
                "title" : "Please enter data",
                "status" : "error",
                "status_response" : 403,
            }

        
    return JsonResponse(
        data=object_return,
        status=object_return["status_response"]
    )