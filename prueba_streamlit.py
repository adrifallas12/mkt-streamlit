import pandas as pd
import streamlit as st

st.title('First Attempt')

st.checkbox('we are cool')
st.radio('Pick your favorite programming language!', ['Python', 'SQL', 'JavaScript', 'C++', "Perl"])
st.selectbox('Pick your name', ['Adriana', 'Jonathan', 'Javier', 'Sofia'])
st.select_slider('How cold is it?', ['Hot', 'Warm', 'Cold', 'Freezing'])