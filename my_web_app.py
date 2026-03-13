import streamlit as st
import pandas as pd
import google.generativeai as genai

# Apni key yahan daalein
API_KEY =
 "gen-lang-client-0289137108"
genai.configure(api_key=API_KEY)

# Data load karein
try:
    df =
 pd.read_csv("master_up_data.csv")
except:
    st.error("Error: 'master_up_data.csv' file nahi
 mili.")

st.title("AI-Powered UP Bhasha Search Engine")

query = st.text_input("Kuch bhi 
search karein ya puchiye:")

if query:
    # 1. Data mein search
    st.write("### Data se jawab:")
    search_result = df[df['sentence'].str.contains(query, case=False,
 na=False)]
    
    if not search_result.empty:
        st.dataframe(search_result)
    else:
        st.write("Data mein match
 nahi mila.")
    
    # 2. AI se jawab
    st.write("### AI ka jawab:")
    model = genai.GenerativeModel('
gemini-1.5-flash')
    response = 
model.generate_content(f"Aap ek 
assistant hain. User ka sawal hai:
 {query}. 
Iska sahi jawab dein.")
    st.write(response.text)