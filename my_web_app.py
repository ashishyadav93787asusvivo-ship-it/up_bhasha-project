import streamlit as st
import pandas as pd
import google.generativeai as genai

# API Key
genai.configure(api_key="AIzaSyCe3kHVefus4fA2ceWv7PvvK74vRifPZYk")

st.title("UP Bhasha AI Search")

# CSV load karein
try:
    df = pd.read_csv("master_up_data.csv")
    query = st.text_input("Apni bhasha mein puchiye:")
    
    if query:
        # CSV Search
        match = df[df['Local Sentence'].str.contains(query, case=False, na=False)]
        if not match.empty:
            st.dataframe(match)
        
        # AI Jawab (Ab hum gemini-pro use kar rahe hain)
        # Sabse stable model call
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(query)
        st.write(response.text)
except Exception as e:
    st.error(f"Error: {e}")
