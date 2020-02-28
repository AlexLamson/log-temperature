# log-temperature
Log indoor temperature / air pressure with a raspberry to a google sheet


## Setup
### 1. Python configuration
[Install Python 3.6](https://installvirtual.com/install-python-3-on-raspberry-pi-raspbian/) (Note: This step can take several hours to run)

Install the required packages: `pip3.6 install gspread oauth2client`


### 2. Make it possible to read from the temperature sensor
[Install Adafruit_Python_BMP python module](https://github.com/adafruit/Adafruit_Python_BMP)

[Enable the I2C protocol feature in Raspberry Pi](https://raspberrypi.stackexchange.com/a/64310/64324)


### 3. Make it possible to read from the temperature sensor
Follow the tutorial [here](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) to get API access to Google Sheets

Put the resulting `client_secret.json` file in this directory

Make sure you set the spreadsheet id and worksheet name in `logger.py`


### 4. Make the script run when the Raspberry Pi turns on
Run `collect_temperature_data.sh` on startup by following the instructions here: https://raspberrypi.stackexchange.com/a/8735/64324
We want it to start on boot, so we need to copy the script to /etc/init.d, check its permissions & register it to run at startup
