import os
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

analyzer = SentimentIntensityAnalyzer()

file_list = sorted(os.listdir('ToneAnalysis/texts'))
positivity = []
negativity = []
for path in file_list:
    file = open(f'ToneAnalysis/texts/{path}')
    text = file.read()
    scores = analyzer.polarity_scores(text)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])
dates = sorted([path.strip('.txt') for path in file_list])

st.header('Diary Tone:')

st.subheader('Positivity')
figure1 = px.line(x=dates, y=positivity, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure1)

st.subheader('Negativity')
figure2 = px.line(x=dates, y=negativity, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure2)
