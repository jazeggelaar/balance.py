import streamlit as st
import json
with open("data.json", "r")as money:
    money1 = json.load(money)
st.write(money1)
if st.button("add"):
    st.switch_page("pages/add2.py")
if st.button("remove"):
    st.switch_page("pages/remove.py")
with open('data.json', 'w')as money:
    json.dump(money1, money)