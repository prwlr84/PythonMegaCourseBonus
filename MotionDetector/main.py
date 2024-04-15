import datetime
import cv2
import streamlit as st

st.title('Motion Detector')
start = st.button('Start Cam')

if start:
    streamlit_img = st.image([])
    video = cv2.VideoCapture(0)

    while True:
        day = datetime.date.today().strftime('%A')
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=day, org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(20, 100, 200), thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=time_now, org=(50,100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 10, 20), thickness=2, lineType=cv2.LINE_AA)

        streamlit_img.image(frame)