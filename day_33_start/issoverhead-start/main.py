import requests, smtplib, schedule, time
from datetime import datetime
from email.mime.text import MIMEText

def send_email():
    my_email = "okikiviolet1@gmail.com"
    my_password = "dautribguvdblwxt"
    content = "Go outside and look up.\nThe iss is overhead."
    to_email = "nelson.okiki@yahoo.com"
    msg = MIMEText(content, "plain", "utf-8")
    msg['Subject'] = "ISS OVERHEAD"
    msg['From'] = my_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=msg.as_string()
            )
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email to {to_email}: {e}")
    except smtplib.SMTPConnectError:
        print("Failed to connect to SMTP server. Check server/port or network.")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Verify email and App Password.")
    except TimeoutError:
        print("Connection timed out. Check internet or firewall settings.")
    except Exception as e:
        print(f"An error occurred: {e}")
def check_iss():
    MY_LAT = 6.482050 # Your latitude
    MY_LONG = 7.501955 # Your longitude
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        #Your position is within +5 or -5 degrees of the ISS position.


        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        current_hour = time_now.hour
        evening_hours = range(19,24)
        morning_hours = range(0,7)

        #If the ISS is close to my current position,
        if ((MY_LAT -5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG -5 <= iss_longitude <= MY_LONG + 5)
                and (current_hour in evening_hours or current_hour in morning_hours)):
            send_email()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
    # and it is currently dark,
    # Then email to tell me to look up.
    # BONUS: run the code every 60 seconds.
schedule.every(60).seconds.do(check_iss)

while True:
    schedule.run_pending()
    time.sleep(1)



