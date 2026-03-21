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
        '''
        http://localhost:8080 is the same as http://api:8080 because the api container is published to the host machine on port 8080.
        This is done in the docker-compose.yml file at the base level of the project.
        The api container is also named "api" in the docker-compose.yml file.
        So, http://api:8080 is the same as http://localhost:8080.
        This is useful because it allows us to use the same URL for the api in the simulator and the browser.
        This is also useful because it allows us to use the same URL for the api in the simulator and the browser.
        '''
        requests.post("http://api:8080/tracks", json=track) # post the track to the api
        print("sent", track) # print the track to the console
    except Exception as e:
        print("error", e) # print the error to the console

    time.sleep(1) # sleep for 1 second
