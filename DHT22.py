import Adafruit_DHT
from firebase import firebase
import time

# Initialize Firebase
firebase = firebase.FirebaseApplication('YOUR_FIREBASE_URL', None)

# Define the sensor pin
sensor_pin = 4  # Example for DHT22, change it according to your sensor

# Function to read sensor data
def read_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, sensor_pin)
    return humidity, temperature

# Main loop
while True:
    humidity, temperature = read_sensor_data()

    if humidity is not None and temperature is not None:
        # Send data to Firebase
        data = {'temperature': temperature, 'humidity': humidity}
        firebase.post('/sensor_data', data)

    # Delay for 10 seconds
    time.sleep(10)