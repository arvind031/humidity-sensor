# Humidity Sensor Readme

## Introduction

This project involves the measurement of humidity and temperature in the environment using a DHT22 sensor. The sensor is interfaced with a Raspberry Pi microcontroller for climate monitoring. The collected data is then sent to a Firebase database for storage and further analysis.

## Components Used

- DHT22 sensor
- Raspberry Pi
- Adafruit_DHT library
- Firebase library

## Code Overview

### 1. Library Imports

The project begins by importing two libraries:
- `Adafruit_DHT` library: Used for reading data from the DHT22 sensor.
- `firebase` library: Used for interacting with the Firebase database.

### 2. Firebase Initialization

The Firebase database is initialized by providing the Firebase project URL. This step is essential to establish a connection between the Raspberry Pi and the Firebase database for data transmission.

### 3. Pin Definition

A session pin is defined to specify the GPIO (General-Purpose Input/Output) pin on the Raspberry Pi to which the DHT22 sensor is connected. This pin is used for data communication between the sensor and the Raspberry Pi.

### 4. `read_sensor_data()` Function

A function called `read_sensor_data()` is defined to read the humidity and temperature values from the DHT22 sensor. This function utilizes the `Adafruit_DHT.read_retry()` method to reliably read data from the sensor. It is likely that this function also handles data formatting and error checking.

### 5. Main Loop

In the main loop of the code, the humidity and temperature of the environment are measured every five seconds using the `read_sensor_data()` function. If the data obtained from the sensor is valid and error-free, it is sent to the Firebase database for storage. This loop ensures continuous monitoring of the climate and data transmission.

## Contributors

- Kasyap Dharanikota (SE20UARI173)
- Manideep Gummadi (SE20UARI174)
- Vikas Verma (SE20UARI175)
- Balaji Arvind (SE20UARI031)

