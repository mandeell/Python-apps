import os
from dotenv import load_dotenv

load_dotenv()  # Call the function to load environment variables
my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")
to_email = os.getenv("TO_EMAIL")