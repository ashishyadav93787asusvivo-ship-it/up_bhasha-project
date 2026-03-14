import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. API Key Setup
API_KEY = "AIzaSyCe3kHVefus4fA2ceWv7PvvK74vRifPZYk"
genai.configure(api_key=API_KEY)

# 2. Data Load (CSV File)
try:
    df = pd.read_csv("master_up_data.csv")
    data_loaded = True
except Exception as e:
    st.error(f"File load nahi hui: {e}")
    data_loaded = False

st.title("UP Bhasha AI Search Engine")
query = st.text_input("Apni bhasha mein puchiye (e.g., Ka bhay?):")

if query:
    # --- Local Data mein Search ---
    st.subheader("Data se jawab:")
    if data_loaded:
        # Aapki file mein 'Local Sentence' column hai
        search_result = df[df['Local Sentence'].str.contains(query, case=False, na=False)]
        
        if not search_result.empty:
            st.dataframe(search_result)
        else:
            st.write("Data mein match nahi mila.")
    
    # --- AI se jawab (Model change kiya hai) ---
    st.subheader("AI ka jawab:")
    try:
        # 'gemini-pro' ki jagah 'gemini-pro-latest' try karein
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Aap UP ki bhashao ke expert hain. Sawal: {query}")
        st.write(response.text)
    except Exception as e:
        st.error(f"AI Error: {e}")