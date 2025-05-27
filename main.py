import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (float(longitude), float(latitude))

parameters = {
    "lat": iss_position[1],
    "lng": iss_position[0],
    "date": "1995-11-09",
    "formatted": 1,
    "tzid": "Africa/Lagos"
}

response_2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_2.raise_for_status()
print(response_2.json())

