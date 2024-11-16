from fastapi import FastAPI
from pydantic import BaseModel
import joblib

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
    dict_f = {
        'appearance': input_features.appearance,
        'minutes_played': input_features.minutes_played,
        'highest_value': input_features.highest_value,
        'current_value': input_features.current_value
    }
    
    features_list = [dict_f[key] for key in sorted(dict_f)]
    
    scaled_features = scaler.transform([features_list])
    
    return scaled_features

@app.post("/predict")
def predict(input_features: InputFeatures):
    processed_data = preprocessing(input_features)
    
    prediction = model.predict(processed_data)
    
    return {"prediction": prediction.tolist()}
