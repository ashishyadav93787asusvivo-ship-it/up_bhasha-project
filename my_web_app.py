import streamlit as st

st.title("Test Mode: UP Bhasha")
st.write("✅ Agar aapko yeh dikh raha hai, toh Streamlit sahi kaam kar raha hai!")

query = st.text_input("Kuch likhiye:")
if query:
    st.write("---")
    st.write(f"Aapne pucha: **{query}**")
    st.write("✅ App ka structure sahi hai, ab hum AI wapas jod sakte hain!")
