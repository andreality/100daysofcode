import requests


PIXELA_URL = "https://pixe.la/v1/users/andreality"
TOKEN = "blargle22%$-"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = PIXELA_URL + "/graphs/pushups"


def attempt_to_add_pixel(date, reps):
    pixel_params = {
        "date": str(date),
        "quantity": str(reps)
    }
    response = requests.post(url=graph_endpoint, json=pixel_params, headers=HEADERS)
    return response


def add_pixel(date, reps):
    success = False
    while success is False:
        response = attempt_to_add_pixel(date, reps=reps)
        print(response)
        if response.status_code == 200:
            success = True
