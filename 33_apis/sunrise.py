import requests
from datetime import datetime


date = str(datetime.now().strftime("%Y-%m-%d"))
parameters = {'lat': 43.45, 'lng': -80.49, 'date': date}

api_request = "https://api.sunrise-sunset.org/json"
response = requests.get(api_request, params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunset)
