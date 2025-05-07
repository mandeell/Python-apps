import os
import json
import schedule
import time
import threading
from datetime import datetime
from twilio.rest import Client
from openai import OpenAI
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from abc import ABC, abstractmethod
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Flask app
flask_app = Flask(__name__)

class MessageGenerator(ABC):
    """Abstract base class for message generators."""
    @abstractmethod
    def generate_message(self, prompt):
        pass

class GrokGenerator(MessageGenerator):
    """Message generator using Grok (xAI API)."""
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_message(self, prompt):
        # Placeholder for xAI API
        try:
            from xai import XAIClient  # Hypothetical import
            client = XAIClient(api_key=self.api_key)
            response = client.generate_text(
                prompt=prompt,
                max_tokens=50,
                temperature=0.7
            )
            return response.text.strip()
        except Exception as e:
            logger.error(f"Grok error: {e}")
            return "Good morning, my love! You make every day brighter."

class OpenAIGenerator(MessageGenerator):
    """Message generator using OpenAI (ChatGPT)."""
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_message(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a romantic assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            return "Good morning, my love! You make every day brighter."

class WhatsAppSender:
    """Class to send WhatsApp messages via Twilio."""
    def __init__(self, account_sid, auth_token, sender_number):
        self.client = Client(account_sid, auth_token)
        self.sender_number = sender_number

    def send_message(self, to_number, message):
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.sender_number,
                to=to_number
            )
            logger.info(f"Message sent at {datetime.now()}: {message.sid}")
        except Exception as e:
            logger.error(f"Error sending message: {e}")

class Scheduler:
    """Class to schedule daily message sending."""
    def __init__(self, time_str, job):
        self.time_str = time_str
        self.job = job
        self.schedule_job()

    def schedule_job(self):
        schedule.every().day.at(self.time_str).do(self.job)

    def update_time(self, new_time):
        self.time_str = new_time
        schedule.clear()
        self.schedule_job()

class GoodMorningApp:
    """Main application class."""
    def __init__(self):
        self.config_file = "config.json"
        self.load_config()
        self.sender = WhatsAppSender(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN"),
            self.config["sender_number"]
        )
        self.generator = self.create_generator()
        self.scheduler = Scheduler(self.config["time"], self.send_daily_message)

    def load_config(self):
        """Load configuration from JSON file or set defaults."""
        default_config = {
            "time": "06:00",
            "prompt": "Create a short, romantic good morning message for my love, under 100 characters.",
            "sender_number": os.getenv("TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886"),
            "receiver_number": os.getenv("RECIPIENT_PHONE", "whatsapp:+1234567890"),
            "use_grok": True
        }
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = default_config
            self.save_config()

    def save_config(self):
        """Save configuration to JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def create_generator(self):
        """Create appropriate message generator based on config."""
        if self.config["use_grok"] and os.getenv("XAI_API_KEY"):
            return GrokGenerator(os.getenv("XAI_API_KEY"))
        elif os.getenv("OPENAI_API_KEY"):
            return OpenAIGenerator(os.getenv("OPENAI_API_KEY"))
        else:
            raise ValueError("No valid API key found for message generation.")

    def send_daily_message(self):
        """Generate and send the daily message."""
        message = self.generator.generate_message(self.config["prompt"])
        self.sender.send_message(self.config["receiver_number"], message)

    def run(self):
        """Run the scheduler."""
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(60)

        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()

# Flask routes
@flask_app.route('/')
def home():
    return "WhatsApp Good Morning App is running!"

@flask_app.route('/config', methods=['GET', 'POST'])
def config():
    app = GoodMorningApp()
    if request.method == 'POST':
        app.config["time"] = request.form['time']
        app.config["prompt"] = request.form['prompt']
        app.config["sender_number"] = request.form['sender_number']
        app.config["receiver_number"] = request.form['receiver_number']
        app.config["use_grok"] = request.form['use_grok'] == 'true'
        app.save_config()
        app.sender = WhatsAppSender(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN"),
            app.config["sender_number"]
        )
        app.generator = app.create_generator()
        app.scheduler.update_time(app.config["time"])
        return redirect(url_for('config'))
    return render_template('config.html', config=app.config)

@flask_app.route('/send_now', methods=['POST'])
def send_now():
    app = GoodMorningApp()
    app.send_daily_message()
    return redirect(url_for('config'))

if __name__ == "__main__":
    app = GoodMorningApp()
    app.run()
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))