import pandas as pd
import streamlit as st
import requests

st.title('First Attempt')

st.checkbox('we are cool')
st.radio('Pick your favorite programming language!', ['Python', 'SQL', 'JavaScript', 'C++', "Perl"])
st.selectbox('Pick your name', ['Adriana', 'Jonathan', 'Javier', 'Sofia'])
st.select_slider('How cold is it?', ['Hot', 'Warm', 'Cold', 'Freezing'])

# upload_file = st.file_uploader("Upload your files", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(uploaded_file)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='test.csv',
    mime='text/csv',
)