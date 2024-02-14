import requests
from common import TOKEN, HEADERS


# create user account
# pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token":"blargle22%$-",
#     "username":"andreality",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# update user account
user_params = {
    "displayName": "andreality",
    # "gravatarIconEmail": "andrea.sweny@gmail.com",
    "pinnedGraphID": "pushups"
}

PIXELA_URL = "https://pixe.la/@andreality"
response = requests.post(url=PIXELA_URL, json=user_params, headers=HEADERS)
print(response.status_code)
