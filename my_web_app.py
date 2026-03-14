import streamlit as st
import google.generativeai as genai

st.title("UP Bhasha AI Search")

# Yahan hum seedha API key daal rahe hain taaki "Secrets" ka jhanjhat khatam ho
# NOTE: Jab app chal jaye, tab ise "Secrets" mein move kar lenge
API_KEY = "AIzaSyBV18ksORYbHlE2uUp3VOPi8N8Jr7IXL7A"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    query = st.text_input("Apni bhasha mein puchiye:")
    if query:
        response = model.generate_content(query)
        st.write("### Jawab:")
        st.write(response.text)
        
except Exception as e:
    st.error(f"Error: {e}")
