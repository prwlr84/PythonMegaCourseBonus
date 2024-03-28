import streamlit as st
from PIL import Image

with st.expander('Start Cam'):
    photo = st.camera_input('Camera')

if photo:
    img = Image.open(photo)
    gray = img.convert('L')
    st.image(gray)