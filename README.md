# Log Temperature
Log temperature / air pressure to a Google Sheet with a Raspberry Pi

![Graph of example data](https://raw.github.com/AlexLamson/log-temperature/master/graph.jpg)


## Setup

### 1. Python configuration
[Install Python 3.6](https://installvirtual.com/install-python-3-on-raspberry-pi-raspbian/) (Note: This step can take several hours to run)

Install the required packages: `pip3.6 install gspread oauth2client`


### 2. Setup the temperature sensor
[Install Adafruit_Python_BMP python module](https://github.com/adafruit/Adafruit_Python_BMP)

[Enable the I2C protocol feature in Raspberry Pi](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi)


### 3. Get access to Google Sheets API
Follow the tutorial [here](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) to get API access to Google Sheets

Put the resulting `client_secret.json` file in this directory

Open `logger.py` and set the `SPREADSHEET_NAME` variable to the title of your spreadsheet.
(You can also specify the worksheet tab name, if you're using a specific tab)


### 4. Running the script
Run `python3.6 logger.py` to get a temperature and pressure reading and log it to the google sheet.


### 5. Scheduling the script
Run `crontab -e` to edit your crontab and add the following line (you may have to adjust the path based on where you cloned the repository). This will make the script run every 5 minutes.

`*/5 * * * * /usr/local/bin/python3.6 /home/pi/log-temperature/logger.py /home/pi/log-temperature/client_secret.json`
