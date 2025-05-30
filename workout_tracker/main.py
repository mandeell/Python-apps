from dotenv import load_dotenv
import os, requests
from datetime import datetime

load_dotenv(dotenv_path=".env")
APP_ID = os.environ.get("NUTRIX_ID")
APP_KEY = os.environ.get("NUTRIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHETTY_API_POST = os.environ.get("SHETTY_API_POST")
SHETTY_API_PUT = os.environ.get("SHETTY_API_PUT")
TOKEN = os.environ.get("TOKEN")



def nutrix():

    exercise = input("Tell me which exercise you did: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "x-remote-user-id": "0",
    }

    exercise_config = {
        "query": exercise
    }

    response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(result)
    return result

def update_shetty():

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    today_date = datetime.now().strftime("%x")
    now_time = datetime.now().strftime("%X")

    for exercises in nutrix()["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercises["name"].title(),
                "duration": exercises["duration_min"],
                "calories": exercises["nf_calories"]
            }
        }

        sheet_response = requests.post(url=SHETTY_API_POST, json=sheet_inputs, headers=bearer_headers)
        print(sheet_response.text)

update_shetty()