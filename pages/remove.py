import streamlit as st
import json
if st.text_input("enter pincode") == "5123":
    with open("data.json", "r")as money:
        money1 = json.load(money)
    new = st.text_input("remove")
    if new != "":
        money1 = str(int(money1)-int(new))
    with open('data.json', 'w')as money:
        json.dump(money1, money)
    st.switch_page("pages/use.py")