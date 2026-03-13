import streamlit as st
import pandas as pd

# 1. Page ki Setting (Layout ko wide karna)
st.set_page_config(page_title="UP Search Engine", layout="wide")

# 2. Styling aur Header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>UP Bhasha Search Engine 🌐</h1>", unsafe_allow_html=True)

# Data load karna
df = pd.read_csv('master_up_data.csv')

# Search Box aur Button
search_query = st.text_input("🔍 Yahan apna shabd likhein:")

if st.button("Search Karein"):
    if search_query:
  import streamlit as st
import pandas as pd
import google.generativeai as genai

# Yahan apni API Key paste karein
API_KEY = "PASTE_YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

# Data load karein
df = pd.read_csv("master_up_data.csv")

st.title("AI-Powered UP Bhasha Search Engine")

query = st.text_input("Kuch bhi search karein ya puchiye:")

if query:
    # 1. Pehle local data mein check karein
    search_result = df[df['sentence'].str.contains(query, case=False, na=False)]
    
    import streamlit as st
import pandas as pd
import google.generativeai as genai

# Yahan apni asli API Key paste karein (AIza se shuru hone wali)
API_KEY = " gen-lang-client-0289137108"
genai.configure(api_key=API_KEY)

# Data load karein
try:
    df = pd.read_csv("master_up_data.csv")
except:
    st.error("Error: 'master_up_data.csv' file nahi mil rahi hai.")

st.title("AI-Powered UP Bhasha Search Engine")

query = st.text_input("Kuch bhi search karein ya puchiye:")

if query:
    # 1. Data mein search karein
    st.write("### Data se jawab:")
    search_result = df[df['sentence'].str.contains(query, case=False, na=False)]
    
    if not search_result.empty:
        st.dataframe(search_result)
    else:
        st.write("Data mein koi match nahi mila.")
    
    # 2. AI se sawal puchiye
    st.write("### AI ka jawab:")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Aap ek assistant hain. User ka sawal hai: {query}. Iska sahi jawab dein.")
    st.write(response.text)