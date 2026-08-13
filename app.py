import streamlit as st
st.write("new here?")
if st.button("yes"):
    st.switch_page("pages/start.py")
if st.button("no"):
    st.switch_page("pages/use.py")