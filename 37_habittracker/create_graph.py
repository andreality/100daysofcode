import requests
from common import PIXELA_URL, TOKEN


# create graph definition

graph_endpoint = PIXELA_URL + "/graphs"
graph_params = {
    "id": "pushups",
    "name": "Pushups Tracker",
    "unit": "reps",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

