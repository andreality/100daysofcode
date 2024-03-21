import requests
from common import PIXELA_URL, TOKEN, HEADERS
from datetime import datetime


graph_endpoint = PIXELA_URL + "/graphs/pushups"
date = datetime.now().strftime("%Y%m%d")


def add_pixel(date, reps):
    pixel_params = {
        "date": str(date),
        "quantity": str(reps)
    }
    response = requests.post(url=graph_endpoint, json=pixel_params, headers=HEADERS)
    return response


reps_history = [('2024-02-01', 49), ('2024-02-02', 54)]

date = 20240203
i = 0
pushups = [55, 0, 50, 60, 63, 0, 76, 84, 100]

while date < 20240212:
    response = add_pixel(date, pushups[i])
    print(response.status_code)
    if response.status_code == 200:
        date += 1
        i += 1






