import gspread
from oauth2client.service_account import ServiceAccountCredentials

import datetime
from time import sleep


def get_worksheet(SPREADSHEET_NAME, WORKSHEET_NAME, CLIENT_SECRET_FILE):
    # use creds to create a client to interact with the Google Drive API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets'
        ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_FILE, scope)
    client = gspread.authorize(creds)

    # find spreadsheet by name and open the desired worksheet
    spreadsheet = client.open(SPREADSHEET_NAME)
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
    return worksheet

def datetime_to_sheets_timestamp(datetime_obj):
    # google sheets uses a special timestamp format
    # this function converts to that special format
    sheets_timestamp = (datetime_obj - datetime.datetime(1899, 12, 30)).total_seconds()/86400
    return sheets_timestamp

def append_row(worksheet, row):
    # append a list of cells to the end of a worksheet
    success = False
    while not success:
        now = datetime.datetime.now()
        timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(now)
        try:
            worksheet.append_row(values=row)
        except Exception as e:
            print(f"[{timestamp}] {e}")
            print("Attempting again in 30 seconds")
            sleep(30)
        else:
            success = True
