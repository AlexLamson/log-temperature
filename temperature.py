from Adafruit_BMP import BMP085

# initialize the weather sensor
sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

def get_sensor_readings():
    # ask the sensor for the temperature and pressure
    temperature_c = sensor.read_temperature()
    temperature_f = float(f"{(temperature_c*9/5) + 32:.2f}")
    altitude_m = sensor.read_altitude()
    pressure_pa = sensor.read_pressure()
    return temperature_c, temperature_f, altitude_m, pressure_pa
