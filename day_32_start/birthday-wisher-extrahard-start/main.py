import pandas as pd, datetime as dt, random, smtplib
from email.mime.text import MIMEText

##################### Extra Hard Starting Project ######################
def email():
    placeholder = "[NAME]"
    data = pd.read_csv('birthdays.csv')
    today_date = dt.datetime.now()
    today_tuple = (today_date.month,today_date.day)

    my_email = "okikiviolet1@gmail.com"
    my_password = "dautribguvdblwxt"
    birthday_people = [row for index, row in data.iterrows()
                       if (row["month"], row["day"]) == today_tuple]

    if not birthday_people:
        print("No birthdays today.")
    else:
        print("Today's birthdays:")
        for row in birthday_people:
            print(f"Name: {row['name']}, Email: {row['email']}")
    print("\n")
    for birthday_person in birthday_people:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path, "r") as file:
            content = file.read()
            content = content.replace(placeholder, birthday_person["name"])
            msg = MIMEText(content, "plain", "utf-8")
            msg['Subject'] = "Happy Birthday"
            msg['From'] = my_email
            msg['To'] = birthday_person["email"]

            try:
                with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=my_password)
                    connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_person["email"],
                    msg=msg.as_string()
                    )
                print("Email sent successfully!")
            except smtplib.SMTPException as e:
                print(f"Failed to send email to {birthday_person['email']}: {e}")
            except smtplib.SMTPConnectError:
                print("Failed to connect to SMTP server. Check server/port or network.")
            except smtplib.SMTPAuthenticationError:
                print("Authentication failed. Verify email and App Password.")
            except TimeoutError:
                print("Connection timed out. Check internet or firewall settings.")
            except Exception as e:
                print(f"An error occurred: {e}")

email()
