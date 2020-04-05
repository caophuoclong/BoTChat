# coding=<UTF-8>
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    diction = {"CT101" : "Lập trình căn bản A", "TN001" : "Vi tích phân A1", "CT172":"Toán rời rạc","ML014" :"Triết Học Mác Lê Nin", "KL001":"Pháp luật đại cương", "SHCVHT":"Sinh hoạt cố vấn"}
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        print('No upcoming events found.')
    for event in events:
        datestart = ""
        dateend = ""
        timestart =""
        timesend=""
        start = event['start'].get('dateTime')
        end = event['end'].get('dateTime')
        for i in range(10):
            datestart += start[i]
            
        for i in range(11,19):
            timestart += start[i]
            timesend += end[i]
        begin = "Ngày: " + datestart + "\nThời gian bắt đầu: " + timestart
        subject = "\nMôn học: " + diction[event['summary']]
        clas = "\nPhòng học: " + event["description"]
        eof = "\nKết thúc: " + timesend
        total = begin + subject + clas + eof
        return total

if __name__ == '__main__':
    main()
        
        
        