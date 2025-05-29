import requests, os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta

ENV_FILE_PATH = "../../../day_35_start/.env"
load_dotenv(dotenv_path=ENV_FILE_PATH)

APH_API_KEY = os.getenv("APH_API_KEY1")
STOCK_API_KEY = os.getenv("STOCK_NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

if not all([APH_API_KEY, STOCK_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TO_PHONE_NUMBER]):
    raise ValueError("Missing environment variables in .env file")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
APH_API = "https://www.alphavantage.co/query"
STOCK_NEWS_API = "https://newsapi.org/v2/everything"


def get_stock_news_api(up_down: str, diff_percent: int):
    # Dynamic date range (yesterday to today)
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    stock_news_params = {
        "apiKey": STOCK_API_KEY,
        "q": COMPANY_NAME,
        "from": yesterday.strftime("%Y-%m-%d"),
        "to": today.strftime("%Y-%m-%d"),
        "sortBy": "popularity",
    }
    try:
        response = requests.get(url=STOCK_NEWS_API, params=stock_news_params, timeout=10)
        response.raise_for_status()
        three_articles = response.json()["articles"][:3]
        for article in three_articles:
            my_message = f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}\n"
            message = client.messages.create(
                to=TO_PHONE_NUMBER,
                from_=TWILIO_PHONE_NUMBER,
                body=my_message
            )
            print(f"Message Status: {message.status}")
    except requests.exceptions.RequestException as e:
        print(f"News API request failed: {e}")
    except Exception as e:
        print(f"Twilio error: {e}")

def aph_api_call(date_str: str):
    aph_params = {
        'apikey': APH_API_KEY,
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
    }
    try:
        response = requests.get(url=APH_API, params=aph_params,timeout=10)
        response.raise_for_status()
        data = response.json()
        if "Time Series (Daily)" in data:
            daily_data = data["Time Series (Daily)"]
            return float(daily_data.get(date_str, {}).get("4. close", 0)) if date_str in daily_data else 0
        else:
            print(f"Alpha Vantage error {data}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Alpha Vantage request failed: {e}")
        return 0

def check_stock():
    # Get dates for yesterday and day before
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    day_before = today - timedelta(days=2)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    day_before_str = day_before.strftime("%Y-%m-%d")

    yesterday_price  = aph_api_call(yesterday_str)
    day_before_price = aph_api_call(day_before_str)

    if yesterday_price == 0 or day_before_price == 0:
        print("Failed to fetch stock prices")
        return

    difference = yesterday_price - day_before_price
    up_down = "🔺" if difference > 0 else "🔻"

    average_price = (yesterday_price + day_before_price) / 2
    diff_percent = round((abs(difference) / average_price) * 100) if average_price != 0 else 0

    if abs(diff_percent) > 5:
        print(f"Stock change: {up_down}{diff_percent}%")
        get_stock_news_api(up_down, diff_percent)

if __name__ == "__main__":
    check_stock()
