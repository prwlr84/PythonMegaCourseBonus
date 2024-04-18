import streamlit as st
import plotly.express as px
import db

conn = db.connect()


st.header('Recent temperature readings')
df = db.fetch_all(conn)
x = [data[0].strftime('%d-%m-%Y %H:%M:%S:%f') for data in df]
y = [data[1] for data in df]
figure = px.line(x=x, y=y, labels={'x': 'Date', 'y': 'Temp'})
st.plotly_chart(figure)
