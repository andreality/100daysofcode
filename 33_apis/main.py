import requests


iss_endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_endpoint)
if response.status_code == 404:
    raise Exception("Resource does not exist.")
elif response.status_code == 402:
    raise Exception("Not authorized to access data.")

data = response.json()
lat = data["iss_position"]["latitude"]
lon = data["iss_position"]["longitude"]

# Response codes:
# 1XX = Hold On
# 2XX = Here You Go
# 3XX = Go Away
# 4XX = You Screwed Up
# 5XX = I Screwed Up
