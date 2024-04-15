import streamlit as st
import plotly.express as px
import pandas as pd

st.header('Happiness Chart')
option = st.selectbox('Select data for the x-axis', ('GDP', 'Happiness', 'Generosity'))
option2 = st.selectbox('Select data to y-axis', ('GDP', 'Happiness', 'Generosity'))

st.subheader(f'{option} and {option2}')

df = pd.read_csv('HappinessDataApp/happy.csv')
x = df[option.lower()]
y = df[option2.lower()]
figure = px.scatter(x=x, y=y, labels={'x': option, 'y': option2})
st.plotly_chart(figure)
