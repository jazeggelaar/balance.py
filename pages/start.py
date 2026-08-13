import streamlit as st
st.write("bring owner with you")
code = st.text_input("enter pincode")
if code == "5123":
    st.switch_page("pages/add.py")