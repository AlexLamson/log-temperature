from sys import argv as args
import datetime
from time import time as current_time

from sheets import get_worksheet, datetime_to_sheets_timestamp, append_row
from temperature import get_sensor_readings


SPREADSHEET_NAME = 'Your Spreadsheet Name Goes Here'
WORKSHEET_NAME = 'Sheet1'

CLIENT_SECRET_FILE = args[1] if len(args) > 1 else 'client_secret.json'
worksheet = get_worksheet(SPREADSHEET_NAME, WORKSHEET_NAME, CLIENT_SECRET_FILE)


# get the current time
now = datetime.datetime.now()
timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(now)

# collect the data
sheets_timestamp = datetime_to_sheets_timestamp(now)
temperature_c, temperature_f, altitude_m, pressure_pa = get_sensor_readings()
data_sample = [sheets_timestamp, temperature_f, temperature_c, pressure_pa, altitude_m]

# append data to the google spreadsheet
append_row(worksheet, data_sample)
print(f"[{timestamp}] appended {temperature_f:.2f} F, {pressure_pa} Pa")
