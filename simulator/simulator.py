import time
import random
import requests

while True:
    track = {
        "latitude": random.uniform(30, 50),
        "longitude": random.uniform(-120, -70),
        "speed": random.uniform(100, 600)
    }

    try:
        requests.post("http://api:8080/tracks", json=track) # post the track to the api
        print("sent", track) # print the track to the console
    except Exception as e:
        print("error", e) # print the error to the console

    time.sleep(1) # sleep for 1 second
