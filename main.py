from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# تحميل النموذج والمقياس
model = joblib.load(r"C:\Users\adeln\Desktop\A\Day-29\knn_model.joblib")
scaler = joblib.load(r"C:\Users\adeln\Desktop\A\Day-29\scaler.joblib")

app = FastAPI()

@app.get("/")
def root():
    return "Welcome To Tuwaiq Academy"

class InputFeatures(BaseModel):
    appearance: int
    minutes_played: int
    highest_value: int
    current_value: int

def preprocessing(input_features: InputFeatures):
    # إنشاء قاموس للميزات
    dict_f = {
        'appearance': input_features.appearance,
        'minutes_played': input_features.minutes_played,
        'highest_value': input_features.highest_value,
        'current_value': input_features.current_value
    }
    
    # تحويل القيم إلى قائمة بالترتيب الصحيح
    features_list = [dict_f[key] for key in sorted(dict_f)]
    
    # قياس الميزات باستخدام المقياس المحمل
    scaled_features = scaler.transform([features_list])
    
    return scaled_features

@app.post("/predict")
def predict(input_features: InputFeatures):
    # معالجة البيانات
    processed_data = preprocessing(input_features)
    
    # إجراء التنبؤ
    prediction = model.predict(processed_data)
    
    return {"prediction": prediction.tolist()}