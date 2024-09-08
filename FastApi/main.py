from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import base64
import io
from PIL import Image
import uvicorn
from fastai.vision.all import (
    load_learner,
    PILImage,
)
import urllib.request
from pathlib import Path
import pickle
# import torch
# import json

app = FastAPI()


# MODEL_URL = "https://drive.google.com/uc?export=download&id=1YXfe4sUA6wQMTkR7DA36lyH1J0Diw9fA"  # Replace with your model URL
MODEL_FILE =  Path("C:\\Users\\Admin\\Desktop\\ProjectEX\\mealmasterApp\\FastApi\\export.pkl")
# MODEL_FILE =  Path(r"C:/Users/Admin/Desktop/ProjectEX/mealmasterApp/FastApi/ML_model40ep.h5")
# urllib.request.urlretrieve(MODEL_URL, "export.pkl")
# learn_inf = load_learner(MODEL_URL, cpu=True)
learn_inf = load_learner(MODEL_FILE, cpu=True)
# model = torch.load('C:/Users/Admin/Desktop/ProjectEX/mealmasterApp/FastApi/export.pkl')
# model.eval()

# # Food menus (consider storing in a database for scalability)
thaimenu=[
"แกงเขียวหวานไก่","แกงเทโพ","แกงเลียง","แกงจืดเต้าหู้หมูสับ","แกงจืดมะระยัดไส้",
"แกงมัสมั่นไก่","แกงส้มกุ้ง","ไก่ผัดเม็ดมะม่วงหิมพานต์","ไข่เจียว","ไข่ดาว",
"ไข่พะโล้","ไข่ลูกเขย","กล้วยบวชชี","ก๋วยเตี๋ยวคั่วไก่","กะหล่ำปลีผัดน้ำปลา",
"กุ้งแม่น้ำเผา","กุ้งอบวุ้นเส้น","ขนมครก","ข้าวเหนียวมะม่วง","ข้าวขาหมู",
"ข้าวคลุกกะปิ","ข้าวซอยไก่","ข้าวผัด","ข้าวผัดกุ้ง","ข้าวมันไก่",
"ข้าวหมกไก่","ต้มข่าไก่","ต้มยำกุ้ง","ทอดมัน","ปอเปี๊ยะทอด",
"ผักบุ้งไฟแดง","ผัดไท","ผัดกะเพรา","ผัดซีอิ๊วเส้นใหญ่","ผัดฟักทองใส่ไข่",
"ผัดมะเขือยาวหมูสับ","ผัดหอยลาย","ฝอยทอง","พะแนงไก่","ยำถั่วพู",
"ยำวุ้นเส้น","ลาบหมู","สังขยาฟักทอง","สาคูไส้หมู","ส้มตำ","หมูปิ้ง","หมูสะเต๊ะ","ห่อหมก"
]

engmenu=[
"Chicken Green Curry","Pork Curry With Morning Glory","Spicy Mixed Vegetable Soup","Pork Chopped Tofu Soup","Stuffed Bitter Gourd Broth",
"Chicken Mussaman Curry","Sour Soup","Stir-Fried Chicken With Chestnuts","Omelet","Fried Egg",
"Egg And Pork In Sweet Brown Sauce","Egg With Tamarind Sauce","Banana In Coconut Milk","Stir-Fried Rice Noodles With Chicken","Fried Cabbage With Fish Sauce",
"Grilled River Prawn","Baked Prawns With Vermicelli","Coconut Rice Pancake","Mango Sticky Rice","Thai Pork Leg Stew",
"Shrimp Paste Fried Rice","Curried Noodle Soup With Chicken","Fried Rice","Shrimp Fried Rice","Steamed Capon In Flavored Rice",
"Thai Chicken Biryani","Thai Chicken Coconut Soup","River Prawn Spicy Soup","Fried Fish-Paste Balls","Deep-Fried Spring Roll",
"Stir-Fried Chinese Morning Glory","Fried Noodle Thai Style With Prawns","Stir-Fried Thai Basil With Minced Pork","Fried Noodle In Soy Sauce","Stir-Fried Pumpkin With Eggs",
"Stir-Fried Eggplant With Soybean Paste Sauce","Stir-Fried Clams With Roasted Chili Paste","Golden Egg Yolk Threads","Chicken Panang ","Thai Wing Beans Salad",
"Spicy Glass Noodle Salad","Spicy Minced Pork Salad","Egg Custard In Pumpkin","Tapioca Balls With Pork Filling","Green Papaya Salad",
"Thai-Style Grilled Pork Skewers","Pork Satay With Peanut Sauce","Steamed Fish With Curry Paste"
]


# Assuming learn is your model and it's loaded here
# from your_model_file import learn

class PredictionResult(BaseModel):
    result: str

@app.post("/predict/", response_model=PredictionResult)
async def predict(image_base64: str):
    try:
        # Decode the base64 string
        base64_decoded = base64.b64decode(image_base64)
        # Convert byte data to a PIL Image
        image = Image.open(io.BytesIO(base64_decoded))
        
        # Assuming you need to save the image temporarily for prediction
        image_path = "temp_image.jpg"
        image.save(image_path)
        
        # Perform prediction (using your own predict function)
        result = learn_inf.predict(image_path)  # Adapt this line to your prediction method

        return PredictionResult(result=str(result))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
# ---------------------------------------------------------------------
# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import JSONResponse
# from PIL import Image
# # from tensorflow.keras.models import load_model
# import tensorflow as tf
# from keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array
# import numpy as np
# from io import BytesIO
# import uvicorn

# # app = FastAPI()

# # Load the model
# # model = tf.keras.models.load_model(r"C:\Users\Admin\Desktop\ProjectEX\mealmasterApp\FastApi\ML_model40ep.h5")
# print(0)
# model = load_model("ML_model40ep.h5")
# print('Suscess')
# # Food menus (consider storing in a database for scalability)
# thaimenu=[
# "แกงเขียวหวานไก่","แกงเทโพ","แกงเลียง","แกงจืดเต้าหู้หมูสับ","แกงจืดมะระยัดไส้",
# "แกงมัสมั่นไก่","แกงส้มกุ้ง","ไก่ผัดเม็ดมะม่วงหิมพานต์","ไข่เจียว","ไข่ดาว",
# "ไข่พะโล้","ไข่ลูกเขย","กล้วยบวชชี","ก๋วยเตี๋ยวคั่วไก่","กะหล่ำปลีผัดน้ำปลา",
# "กุ้งแม่น้ำเผา","กุ้งอบวุ้นเส้น","ขนมครก","ข้าวเหนียวมะม่วง","ข้าวขาหมู",
# "ข้าวคลุกกะปิ","ข้าวซอยไก่","ข้าวผัด","ข้าวผัดกุ้ง","ข้าวมันไก่",
# "ข้าวหมกไก่","ต้มข่าไก่","ต้มยำกุ้ง","ทอดมัน","ปอเปี๊ยะทอด",
# "ผักบุ้งไฟแดง","ผัดไท","ผัดกะเพรา","ผัดซีอิ๊วเส้นใหญ่","ผัดฟักทองใส่ไข่",
# "ผัดมะเขือยาวหมูสับ","ผัดหอยลาย","ฝอยทอง","พะแนงไก่","ยำถั่วพู",
# "ยำวุ้นเส้น","ลาบหมู","สังขยาฟักทอง","สาคูไส้หมู","ส้มตำ","หมูปิ้ง","หมูสะเต๊ะ","ห่อหมก"
# ]

# engmenu=[
# "Chicken Green Curry","Pork Curry With Morning Glory","Spicy Mixed Vegetable Soup","Pork Chopped Tofu Soup","Stuffed Bitter Gourd Broth",
# "Chicken Mussaman Curry","Sour Soup","Stir-Fried Chicken With Chestnuts","Omelet","Fried Egg",
# "Egg And Pork In Sweet Brown Sauce","Egg With Tamarind Sauce","Banana In Coconut Milk","Stir-Fried Rice Noodles With Chicken","Fried Cabbage With Fish Sauce",
# "Grilled River Prawn","Baked Prawns With Vermicelli","Coconut Rice Pancake","Mango Sticky Rice","Thai Pork Leg Stew",
# "Shrimp Paste Fried Rice","Curried Noodle Soup With Chicken","Fried Rice","Shrimp Fried Rice","Steamed Capon In Flavored Rice",
# "Thai Chicken Biryani","Thai Chicken Coconut Soup","River Prawn Spicy Soup","Fried Fish-Paste Balls","Deep-Fried Spring Roll",
# "Stir-Fried Chinese Morning Glory","Fried Noodle Thai Style With Prawns","Stir-Fried Thai Basil With Minced Pork","Fried Noodle In Soy Sauce","Stir-Fried Pumpkin With Eggs",
# "Stir-Fried Eggplant With Soybean Paste Sauce","Stir-Fried Clams With Roasted Chili Paste","Golden Egg Yolk Threads","Chicken Panang ","Thai Wing Beans Salad",
# "Spicy Glass Noodle Salad","Spicy Minced Pork Salad","Egg Custard In Pumpkin","Tapioca Balls With Pork Filling","Green Papaya Salad",
# "Thai-Style Grilled Pork Skewers","Pork Satay With Peanut Sauce","Steamed Fish With Curry Paste"
# ]

# # Define class labels
# class_labels = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']

# # Function to preprocess the image
# def preprocess_image(image: Image.Image) -> np.ndarray:
#     image = image.resize((224, 224))
#     image = img_to_array(image)
#     image = np.expand_dims(image, axis=0)
#     image /= 255.0
#     return image

# # @app.post("/predict/")
# # async def predict(file: UploadFile = File(...)):
# #     # Read and preprocess the image
# #     image = Image.open(BytesIO(await file.read()))
# #     processed_image = preprocess_image(image)

# #     # Make a prediction
# #     predictions = model.predict(processed_image)
# #     predicted_class = class_labels[np.argmax(predictions)]

# #     # Return the prediction as JSON
# #     return JSONResponse(content={"prediction": predicted_class})

# if __name__ == "__main__":
#     path = 'panang.jpg'
#     image = Image.open(path)
#     print(1)
#     processed_image = preprocess_image(image)
#     print(2)
#     predictions = model.predict(processed_image)
#     print(3)
#     predicted_class = class_labels[np.argmax(predictions)]
#     print(4)
#     print(predicted_class)
#     # uvicorn.run(app, host="0.0.0.0", port=8000)

# # @app.get("/")
# # def read_root():
# #     return {"message": "Welcome to the food classification API. Use the /predict/ endpoint to upload an image and get predictions."}
