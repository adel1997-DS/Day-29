import streamlit as st
import requests

st.title("التنبؤ باستخدام الموديل")

# إدخال البيانات
appearance = st.number_input("Appearance", min_value=0)
minutes_played = st.number_input("Minutes Played", min_value=0)
highest_value = st.number_input("Highest Value", min_value=0)
current_value = st.number_input("Current Value", min_value=0)

if st.button("توقع"):
    # بيانات الإدخال
    data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "highest_value": highest_value,
        "current_value": current_value
    }
    try:
        # إرسال الطلب إلى FastAPI المحلي
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"التوقع: {prediction}")
        else:
            st.error(f"خطأ في API: {response.status_code}")
    except Exception as e:
        st.error(f"خطأ في الاتصال بـ API: {e}")
