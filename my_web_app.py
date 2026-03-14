import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("Debug Mode: UP Bhasha")

# 1. API Setup
API_KEY = "AIzaSyAjZO2CBWOr1rsFgT94LgfGgT3wVVFGcoo"
genai.configure(api_key=API_KEY)
st.write("Step 1: API Configuration Done.")

# 2. Model Init
model = genai.GenerativeModel('gemini-1.5-flash')
st.write("Step 2: Model Initialized.")

query = st.text_input("Kuch puchiye:")

if query:
    st.write(f"Step 3: User ne pucha - {query}")
    
    # 3. AI Call
    try:
        st.write("Step 4: AI se contact kar rahe hain...")
        response = model.generate_content(f"Explain in Hindi: {query}")
        st.write("AI Jawab:", response.text)
    except Exception as e:
        st.error(f"Step 4 ERROR: {e}")          
