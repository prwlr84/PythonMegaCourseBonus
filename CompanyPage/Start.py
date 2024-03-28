import streamlit as st
import pandas as ps
from faker import Faker as fkr

st.set_page_config(layout='wide')

st.header('The Best Company')
content_h = fkr().paragraph()
st.write(content_h)

st.subheader('Our Team')


col1, spacer, col2, spacer2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = ps.read_csv('data.csv')
with col1:
    for i, row in df[0::3].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'].title())
        st.image('images/' + row['image'])
with col2:
    for i, row in df[1::3].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'].title())
        st.image('images/' + row['image'])
with col3:
    for i, row in df[2::3].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'].title())
        st.image('images/' + row['image'])



if __name__ == '__main__':
    print('main')