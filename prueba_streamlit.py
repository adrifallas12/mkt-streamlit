import pandas as pd
import streamlit as st
import requests

st.title('First Attempt')

st.checkbox('we are cool')
st.radio('Pick your favorite programming language!', ['Python', 'SQL', 'JavaScript', 'C++', "Perl"])
st.selectbox('Pick your name', ['Adriana', 'Jonathan', 'Javier', 'Sofia'])
st.select_slider('How cold is it?', ['Hot', 'Warm', 'Cold', 'Freezing'])

upload_file = st.file_uploader("Upload your files", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if upload_file is None:
    dataframe = pd.read_csv(upload_file)
    st.table(dataframe)