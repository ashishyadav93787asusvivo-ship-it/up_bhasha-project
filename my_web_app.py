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
        res = df[df['Local Sentence'].str.contains(search_query, case=False, na=False)]
        
        if not res.empty:
            st.success(f"✅ {len(res)} results mile:")
            # Table ko highlight karna
            st.dataframe(res, use_container_width=True)
        else:
            st.error("❌ Nahi mila, kuch aur try kariye!")
    else:
        st.warning("⚠️ Please pehle koi shabd type karein.")