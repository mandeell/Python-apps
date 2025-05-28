import requests, smtplib, schedule, time, os
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv
from typing import Optional  # Import Optional for type hinting

# Load environment variables
load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")
MY_LAT = 6.482050  # Your latitude
MY_LONG = 7.501955  # Your longitude
COOLDOWN_MINUTES = 60
last_email_time: Optional[datetime] = None

def send_email():
    """Send an email notification when the ISS is overhead."""
    global last_email_time
    current_time = datetime.now()
    if last_email_time is None or (current_time - last_email_time).total_seconds() / 60 >= COOLDOWN_MINUTES:
        content = "Go outside and look up.\nThe iss is overhead."
        to_email = "nelson.okiki@yahoo.com"
        msg = MIMEText(content, "plain", "utf-8")
        msg['Subject'] = "ISS OVERHEAD"
        msg['From'] = MY_EMAIL
        msg['To'] = TO_EMAIL

        try:
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=to_email,
                    msg=msg.as_string()
                )
            print("Email sent successfully!")

        except smtplib.SMTPException as e:
            print(f"Failed to send email to {TO_EMAIL}: {e}")
        except smtplib.SMTPConnectError:
            print("Failed to connect to SMTP server. Check server/port or network.")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Verify email and App Password.")
        except TimeoutError:
            print("Connection timed out. Check internet or firewall settings.")
        except Exception as e:
            print(f"An error occurred: {e}")

def is_iss_close():
    """Check if the ISS is within ±5 degrees of the user's location."""
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json",timeout=10)
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
    except requests.exceptions.RequestException as e:
        print(f"Failed to ISS Position: {e}")
        return False

def is_night():
    """Check if it is currently nighttime at the user's location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour

        return time_now >= sunset or time_now <= sunrise
    except requests.exceptions.RequestException as e:
        print(f"Failed to get sunrise and sunset data: {e}")
        return False

def check_iss_and_night():
    """Check if the ISS is overhead, and it's nighttime, then send an email."""
    if is_iss_close() and is_night():
        send_email()

schedule.every(60).seconds.do(check_iss_and_night)

while True:
    schedule.run_pending()
    time.sleep(min(schedule.idle_seconds() or 1, 1))



