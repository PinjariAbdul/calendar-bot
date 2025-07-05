from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'service_account.json'
CALENDAR_ID = os.getenv("CALENDAR_ID")
DELEGATED_EMAIL = os.getenv("DELEGATED_EMAIL")  # Load separately

# Delegate access to the user's Gmail calendar
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
).with_subject(DELEGATED_EMAIL)

service = build('calendar', 'v3', credentials=credentials)

def book_meeting(title, start_time, end_time, description=""):
    event = {
        'summary': title,
        'description': description,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
    }
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"Creating event for: {CALENDAR_ID}, as {DELEGATED_EMAIL}")

    return event.get("htmlLink")