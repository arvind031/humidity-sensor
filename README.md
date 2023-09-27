# humidity-sensor
We are measuring the humidity and temperature of the environment using DHT22 sensor

DHT22

DHT22 is digital and humidity sensors.
We have interfaced with the microcontoller Raspberri Pi for climate monitoring

Code:

First we have imported Adafruit_DHT and firebase library.
Next the firebase is initialed by providing the firebase project URL.
Next, session pin is defined.
read_sensor_data() function is defined which will be used to read the humidity and temperature values using Adafruit_DHT.read_retry().
Finally, in the main loop we measure the humidity and temperature of the environment every five seconds using read_sensor_data() function and if the data is valid we send it to the Firebase database.
BY 
Kasyap Dharanikota Se20UARI173
Manideep Gummadi SE20UARI174
Vikas Verma SE20UARi175
Balaji Arvind Se20uari031
