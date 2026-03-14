import streamlit as st
import pandas as pd
import google.generativeai as genai

# API Key - Isse quotes ke andar hi rehne dein
API_KEY = "AIzaSyAf60yEbSbKg-DHtU0U-FRa2mlVFs4uOvw"
genai.configure(api_key=API_KEY)

# CSV Data Load karne ki koshish
try:
    df = pd.read_csv("master_up_data.csv")
    data_loaded = True
except Exception as e:
    st.error(f"CSV Load nahi ho payi: {e}")
    data_loaded = False

st.title("UP Bhasha AI Search Engine")

query = st.text_input("Apni bhasha mein kuch likhein (e.g., Ka bhay?):")

if query:
    # 1. Excel Data mein search
    st.subheader("Local Data se Khoja gaya:")
    if data_loaded:
        # 'Local Sentence' wahi naam hai jo aapne Excel mein dikhaya tha
        match = df[df['Local Sentence'].str.contains(query, case=False, na=False)]
        
        if not match.empty:
            st.success("Humein data mein match mila!")
            st.dataframe(match)
        else:
            st.warning("Data mein match nahi mila, AI se jawab le rahe hain...")

    # 2. Direct AI se Jawab
    st.subheader("AI Assistant ka Jawab:")
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Aap UP ki bhashao ke expert hain. User ka sawal hai: '{query}'. Iska arth aur sahi jawab dein."
        response = model.generate_content(prompt)
        st.info(response.text)
    except Exception as e:
        st.error(f"AI error: {e}")