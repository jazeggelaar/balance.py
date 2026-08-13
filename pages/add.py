import streamlit as st
import json
new = st.text_input("add")
if new != "":
    with open('data.json', 'w')as money:
        json.dump(new, money)
    st.switch_page("pages/use.py")