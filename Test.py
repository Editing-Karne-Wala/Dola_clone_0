from googleapiclient.discovery import build
import pickle
import datetime

# Load saved credentials
with open("token.pkl", "rb") as token:
    creds = pickle.load(token)

# Build the service
service = build("calendar", "v3", credentials=creds)

# Create an event
event = {
    'summary': 'Test Event from Clone Dola AI',
    'location': 'Home',
    'description': 'This is a test event created from Python.',
    'start': {
        'dateTime': '2025-05-14T14:00:00',
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': '2025-05-14T15:00:00',
        'timeZone': 'Asia/Kolkata',
    },
}

# Insert the event
event = service.events().insert(calendarId='primary', body=event).execute()
print(f"✅ Event created: {event.get('htmlLink')}")
