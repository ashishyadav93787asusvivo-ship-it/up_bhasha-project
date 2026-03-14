import streamlit as st
import google.generativeai as genai

# Streamlit secrets ka use karein (yahan key nahi likhni hai)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("UP Bhasha AI Search")
query = st.text_input("Kuch puchiye:")

if query:
    try:
        response = model.generate_content(f"Answer: {query}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")