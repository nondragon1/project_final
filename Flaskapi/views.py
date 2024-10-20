from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import tensorflow as tf
from PIL import Image, UnidentifiedImageError
import numpy as np
import io , os
from pathlib import Path
# from keras.models import load_model
# from keras.layers import BatchNormalization

# โหลดโมเดล
model_path = "/app/Flaskapi/ML_model40ep.h5"
model = tf.keras.models.load_model(model_path, compile=False)
# model = load_model('C:/Users/Admin/Desktop/ProjectEX/mealmasterApp/Flaskapi/ML_model40ep.h5', custom_objects={'BatchNormalization': BatchNormalization})
def preprocess_image(uploaded_file):
    try:
        img = Image.open(uploaded_file)
        img = img.resize((150, 150))  # ปรับขนาดให้ตรงกับที่โมเดลต้องการ
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        return img_array
    except UnidentifiedImageError:
        return None

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

@api_view(['GET', 'POST'])
def predict(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file part in the request'}, status=400)

        file = request.FILES['file']

        if file.name == '':
            return JsonResponse({'error': 'No selected file'}, status=400)

        processed_image = preprocess_image(file)

        if processed_image is None:
            return JsonResponse({'error': 'Cannot process the uploaded file as an image'}, status=400)

        try:
            predictions = model.predict(processed_image)
            class_labels = [['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']]
            # print(f"Predictions: {predictions}")  # Debugging line
            # print(f"Predictions Type: {type(predictions)}")  # Debugging line
            # print(f"Predictions Shape: {predictions.shape}")  # Debugging line
            
            predicted_class = class_labels[np.argmax(predictions)]
            confidence = np.max(predictions) * 100
            
            
             # Display the prediction
            show = thaimenu[predicted_class]

            return JsonResponse({'prediction': show, 'confidence': confidence})
        except Exception as e:
            return JsonResponse({'error': f'Prediction error: {str(e)}'}, status=500)
    return render(request, "frontend/predict.html")


# --------------------------------------------------------------------------
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.layers import BatchNormalization
# from PIL import Image, UnidentifiedImageError
# import numpy as np
# import io

# # Load the model with custom objects
# model_path = r'C:\Users\Admin\Desktop\ProjectEX\mealmasterApp\Flaskapi\ML_model40ep.h5'
# custom_objects = {'BatchNormalization': BatchNormalization}
# model = load_model(model_path, custom_objects=custom_objects)

# def preprocess_image(uploaded_file):
#     try:
#         img = Image.open(uploaded_file)
#         img = img.resize((150, 150))  # Resize to match the model input requirements
#         img_array = np.array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array = img_array / 255.0  # Normalize to [0, 1]
#         return img_array
#     except UnidentifiedImageError:
#         return None

# # Convert dict for class labels to Thai menu
# thaimenu = {
#     "00": "แกงเขียวหวานไก่", "01": "แกงเทโพ", "02": "แกงเลียง", "03": "แกงจืดเต้าหู้หมูสับ",
#     "04": "แกงจืดมะระยัดไส้", "05": "แกงมัสมั่นไก่", "06": "แกงส้มกุ้ง", "07": "ไก่ผัดเม็ดมะม่วงหิมพานต์",
#     "08": "ไข่เจียว", "09": "ไข่ดาว", "10": "ไข่พะโล้", "11": "ไข่ลูกเขย", "12": "กล้วยบวชชี",
#     "13": "ก๋วยเตี๋ยวคั่วไก่", "14": "กะหล่ำปลีผัดน้ำปลา", "15": "กุ้งแม่น้ำเผา", "16": "กุ้งอบวุ้นเส้น",
#     "17": "ขนมครก", "18": "ข้าวเหนียวมะม่วง", "19": "ข้าวขาหมู", "20": "ข้าวคลุกกะปิ", "21": "ข้าวซอยไก่",
#     "22": "ข้าวผัด", "23": "ข้าวผัดกุ้ง", "24": "ข้าวมันไก่", "25": "ข้าวหมกไก่", "26": "ต้มข่าไก่",
#     "27": "ต้มยำกุ้ง", "28": "ทอดมัน", "29": "ปอเปี๊ยะทอด", "30": "ผักบุ้งไฟแดง", "31": "ผัดไท",
#     "32": "ผัดกะเพรา", "33": "ผัดซีอิ๊วเส้นใหญ่", "34": "ผัดฟักทองใส่ไข่", "35": "ผัดมะเขือยาวหมูสับ",
#     "36": "ผัดหอยลาย", "37": "ฝอยทอง", "38": "พะแนงไก่", "39": "ยำถั่วพู", "40": "ยำวุ้นเส้น",
#     "41": "ลาบหมู", "42": "สังขยาฟักทอง", "43": "สาคูไส้หมู", "44": "ส้มตำ", "45": "หมูปิ้ง",
#     "46": "หมูสะเต๊ะ", "47": "ห่อหมก"
# }

# @api_view(['GET', 'POST'])
# def predict(request):
#     if request.method == 'POST':
#         if 'file' not in request.FILES:
#             return JsonResponse({'error': 'No file part in the request'}, status=400)

#         file = request.FILES['file']

#         if file.name == '':
#             return JsonResponse({'error': 'No selected file'}, status=400)

#         processed_image = preprocess_image(file)

#         if processed_image is None:
#             return JsonResponse({'error': 'Cannot process the uploaded file as an image'}, status=400)

#         try:
#             predictions = model.predict(processed_image)
#             class_labels = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
#                             '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
#                             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44',
#                             '45', '46', '47']

#             predicted_class = class_labels[np.argmax(predictions)]
#             confidence = np.max(predictions) * 100

#             # Display the prediction
#             show = thaimenu[predicted_class]

#             return JsonResponse({'prediction': show, 'confidence': confidence})
#         except Exception as e:
#             return JsonResponse({'error': f'Prediction error: {str(e)}'}, status=500)
#     return render(request, "frontend/predict.html")
