import requests


PIXELA_URL = "https://pixe.la/v1/users/andreality"
TOKEN = "blargle22%$-"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = PIXELA_URL + "/graphs/pushups"


def add_pixel(date, reps):
    pixel_params = {
        "date": str(date),
        "quantity": str(reps)
    }
    response = requests.post(url=graph_endpoint, json=pixel_params, headers=HEADERS)
    return response

