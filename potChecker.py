import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#Creating the connection to the neopixel board

#Creates a pointer for the bus that the analog to digital board is using.
i2c = busio.I2C(board.SCL, board.SDA)

#Creating an object for the analog to digital converter using the bus object created
ads = ADS.ADS1015(i2c)

#Create an input for the specific channels we'll be using
channel = list(range(4))
for analogBoardInput in range(4):
    channel[analogBoardInput] = AnalogIn(ads, analogBoardInput)

print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

while True:
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(channel[0].value, channel[1].value, channel[2].value, channel[3].value))
    # Pause for half a second.
    time.sleep(0.5)
