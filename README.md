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

Open `logger.py` and set the `SPREADSHEET_NAME` variable to the title of your spreadsheet. (You can also specify the worksheet tab name, if you're using a specific tab)


### 4. Running the script
Run `collect_temperature_data.sh` to start writing the current temperature and pressure to your Google sheet, once per minute.


### 5. (Optional) Make the script run when the Raspberry Pi turns on
We want it to start on boot, so we need to copy the script to `/etc/init.d`, check its permissions & register it to run at startup.

```
sudo cp collect_temperature_data.sh /etc/init.d/collect_temperature_data.sh
sudo chmod 755 /etc/init.d/collect_temperature_data.sh
sudo update-rc.d collect_temperature_data.sh defaults
```
