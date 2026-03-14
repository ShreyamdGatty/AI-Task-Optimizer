import streamlit as st

from src.text_emotion import detect_text_emotion
from src.task_recommendation import recommend_task
from src.alerts import check_stress
from utils.data_privacy import anonymize_employee

st.title("AI Powered Task Optimizer")

name = st.text_input("Employee Name")

text = st.text_area("Enter employee message")

if st.button("Analyze Emotion"):

    emotion = detect_text_emotion(text)

    task = recommend_task(emotion)

    alert = check_stress(emotion)

    employee_id = anonymize_employee(name)

    st.write("Employee ID:", employee_id)

    st.write("Detected Emotion:", emotion)

    st.write("Recommended Task:", task)

    st.write(alert)