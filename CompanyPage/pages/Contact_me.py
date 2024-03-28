import streamlit as st
import pandas as ps
from send_email import send_email

st.header('Contact me!')

topics = ps.read_csv('topics.csv')

with st.form(key='form'):
    email = st.text_input('Email')
    topic = st.selectbox('Topic', options=topics)
    text = st.text_area('Message')
    button = st.form_submit_button('Submit')
    message = f'''\
Subject: New message from {email} about {topic}

From: {email}
{text}
'''
    if button:
        send_email(message)
