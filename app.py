# app.py

import streamlit as st
import joblib
from spam_detector import preprocess

model = joblib.load('spam_model.pkl')

st.title("📧 Email Spam Detector")

user_input = st.text_area("Enter your message")

if st.button("Predict"):
    processed = preprocess(user_input)
    prediction = model.predict([processed])
    result = "🚫 Spam" if prediction[0] == 1 else "✅ Not Spam"
    st.subheader(f"Result: {result}")
