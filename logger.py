from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import datetime
from time import sleep
from Adafruit_BMP import BMP085
from time import time as current_time


SPREADSHEET_NAME = 'Your Spreadsheet Name Goes Here'
WORKSHEET_NAME = 'Sheet1'

CLIENT_SECRET_FILE = 'client_secret.json'


# initialize the weather sensor
sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)


# google expires your login after an hour
last_refresh = 0
worksheet = None
def get_sheet():
    global last_refresh, worksheet

    # if it's been 55 minutes since our last refresh, request a new auth token
    if worksheet is None or current_time() >= last_refresh + (60*55):
        print("regenerating auth token")
        last_refresh = current_time()

        # use creds to create a client to interact with the Google Drive API
        scope = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/spreadsheets'
            ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_FILE, scope)
        client = gspread.authorize(creds)

        # Find spreadsheet by name and open the desired worksheet
        spreadsheet = client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        return worksheet
    else:
        return worksheet


# over and over, sample the atmosphere & append it to the google sheet
while True:
    # get the current time
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    sheets_timestamp = (datetime.datetime.now() - datetime.datetime(1899, 12, 30)).total_seconds()/86400

    # get the sensor readings
    altitude_pa = sensor.read_altitude()
    temperature_c = sensor.read_temperature()
    temperature_f = float(f"{(temperature_c*9/5) + 32:.2f}")

    # append data to google spreadsheet
    success = False
    while not success:
        try:
            data_sample = [sheets_timestamp, temperature_f, temperature_c, altitude_pa]
            get_sheet().append_row(values=data_sample)
            print(f"[{timestamp}] appended {temperature_f}, {altitude_pa:.2f}")
        except Exception as e:
            print(f"[{timestamp}] {e}")
            print("Attempting again in 30 seconds")
            last_refresh = 0
            sleep(30)
        else:
            success = True

    # wait a bit before sending the next reading
    sleep(60)
