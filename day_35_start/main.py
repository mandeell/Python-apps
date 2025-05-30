import requests,os
from twilio.rest import Client
from dotenv import load_dotenv

ENV_FILE_PATH = "../.env"
load_dotenv(dotenv_path=ENV_FILE_PATH)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.getenv("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

weather_param = {
    "appid": OWM_API_KEY,
    "lat": "6.482051",
    "lon": "7.501940",
    "cnt": 4
}

weather_response = requests.get(url=OWM_Endpoint, params=weather_param)
weather_response.raise_for_status()
weather_data = weather_response.json()["list"][0]["weather"][0]["id"]

will_rain = False

for my_id in range(0,4):
    weather_data = weather_response.json()["list"][my_id]["weather"][0]["id"]
    if weather_data < 700:
        will_rain = True
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body="You don try go sleep bros"
    )
    print(message.status)

