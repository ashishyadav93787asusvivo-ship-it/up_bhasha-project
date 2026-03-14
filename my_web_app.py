import streamlit as st
import pandas as pd
import google.generativeai as genai

# API Key
genai.configure(api_key="AIzaSyCe3kHVefus4fA2ceWv7PvvK74vRifPZYk")

# 1. Model define karna
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("UP Bhasha AI Search")

# CSV Load
try:
    df = pd.read_csv("master_up_data.csv")
    query = st.text_input("Kuch puchiye:")
    
    if query:
        # CSV Search
        match = df[df['Local Sentence'].str.contains(query, case=False, na=False)]
        if not match.empty:
            st.write("### Data se jawab:")
            st.dataframe(match)
        
        # AI Answer - Naye tarike se call
        st.write("### AI Assistant:")
        try:
            response = model.generate_content(f"Explain this in simple Hindi: {query}")
            st.write(response.text)
        except Exception as ai_err:
            # Yahan hum asli error ko print karenge
            st.error(f"DEBUG ERROR: {ai_err}")