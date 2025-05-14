from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def create_calendar_event(event_details):
    SERVICE_ACCOUNT_FILE = r"C:\Users\shiny\Documents\Dola_CLONE\credentials.json"
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build("calendar", "v3", credentials=credentials)

    event = {
        'summary': event_details['summary'],
        'start': {
            'dateTime': event_details['start'],
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': event_details['end'],
            'timeZone': 'Asia/Kolkata',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink', 'Event Created')
