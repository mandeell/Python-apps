import smtplib, datetime as dt, random

day_of_the_week = dt.datetime.now().weekday()
with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    random_quotes = random.choice(quotes)

my_email = "okikiviolet1@gmail.com"
my_password = "dautribguvdblwxt"
to_email = "nelson.okiki@yahoo.com"


if day_of_the_week == 1:
    try:
        # Connect with increased timeout (10 seconds)
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Monday Motivation\n\n{random_quotes}"
            )
        print("Email sent successfully!")
    except smtplib.SMTPConnectError:
        print("Failed to connect to SMTP server. Check server/port or network.")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Verify email and App Password.")
    except TimeoutError:
        print("Connection timed out. Check internet or firewall settings.")
    except Exception as e:
        print(f"An error occurred: {e}")



