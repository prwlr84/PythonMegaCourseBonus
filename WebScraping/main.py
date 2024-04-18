import time
from datetime import datetime

import requests
import selectorlib

from WebScraping import db

URL = 'https://programmer100.pythonanywhere.com'
conn = db.connect()


def scrape():
    response = requests.get(URL)
    text = response.text
    return text


def parse(text):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yml')
    value = extractor.extract(text)['temp']
    return value


if __name__ == '__main__':
    counter = 0
    while True and counter < 100:
        c_time = datetime.now()
        s = scrape()
        t = parse(s)
        db.insert(conn, [tuple((c_time, t))])
        counter += 1

        time.sleep(2)
