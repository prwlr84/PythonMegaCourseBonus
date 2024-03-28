import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(msg):
    host = 'smtp.google.com'
    port = 465
    user = os.getenv('EMAIL')
    pw = os.getenv('PW')
    context = ssl.create_default_context()
    receiver = user

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, pw)
        server.sendmail(user, receiver, msg)
