import streamlit as st
import requests

# عنوان API المنشور
api_url = "https://your-fastapi-app.onrender.com/predict"  # ضع رابط FastAPI هنا

# واجهة المستخدم في Streamlit
st.title("تطبيق التنبؤ")

# المدخلات
appearance = st.number_input("عدد مرات اللعب", min_value=0)
minutes_played = st.number_input("عدد الدقائق", min_value=0)
highest_value = st.number_input("أعلى قيمة", min_value=0)
current_value = st.number_input("القيمة الحالية", min_value=0)

if st.button("تنبؤ"):
    input_data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "highest_value": highest_value,
        "current_value": current_value,
    }
    try:
        response = requests.post(api_url, json=input_data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"التنبؤ: {prediction}")
        else:
            st.error("خطأ في الاتصال بـ API.")
    except Exception as e:
        st.error(f"خطأ: {e}")
