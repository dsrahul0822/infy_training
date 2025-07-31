import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from router.query_router import handle_user_query

st.set_page_config(page_title="EdTech Bot", page_icon="🎓", layout="centered")

st.title("🎓 EdTech Support Bot")
st.write("Hi! I can help with **FAQs**, **Technical Issues**, and **Billing Issues**.")

# User input fields
user_email = st.text_input("Enter your email:")
user_query = st.text_area("Describe your issue or ask a question:")

if st.button("Submit Query"):
    if not user_email or not user_query:
        st.warning("Please provide both email and query.")
    else:
        with st.spinner("Processing your request..."):
            response = handle_user_query(user_query, user_email)
        st.success("Response Generated ✅")
        st.write(response)
