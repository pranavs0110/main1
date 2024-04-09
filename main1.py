import streamlit as st

with st.container(height=300,border=True):
    answer=st.radio("Do You Want To Make YOUR website",["Yes","No"],index=None)
    con_num=st.number_input("Contact number ",step=1)


