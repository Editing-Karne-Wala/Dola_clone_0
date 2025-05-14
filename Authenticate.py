from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import webbrowser
import os

# Custom browser path
browser_path = r'C:\Program Files\Mozilla Firefox\beufbekfebkfer.exe'
webbrowser.register('firefox-esr', None, webbrowser.BackgroundBrowser(browser_path))
webbrowser.get('firefox-esr').open_new

# OAuth flow with Calendar scope
SCOPES = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file(
    r'C:\Users\shiny\Downloads\credentials.json', SCOPES)
creds = flow.run_local_server(port=0, open_browser=True)

# Save token for reuse
with open('token.pkl', 'wb') as token:
    pickle.dump(creds, token)
