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
        requests.post("http://api:8080/tracks", json=track)
        print("sent", track)
    except Exception as e:
        print("error", e)

    time.sleep(1)
