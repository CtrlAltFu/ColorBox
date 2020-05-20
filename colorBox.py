import board
import busio
import neopixel
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#GPIO pin used for the neoPixel. Recommended pins are 18, D10, D12
neoPixelPin = 18

#Creating the connection to the neopixel board
pixels = neopixel.NeoPixel(board.D18, 8)

#Creates a pointer for the bus that the analog to digital board is using.
i2c = busio.I2C(board.SCL, board.SDA)

#Creating an object for the analog to digital converter using the bus object created
ads = ADS.ADS1015(i2c)

#Create an input for the specific channels we'll be using
channel = list(range(4))
for analogBoardInput in range(4):
    channel[analogBoardInput] = AnalogIn(ads, analogBoardInput)

#Function that will actually change the colors, giving it a default value of white so that you know it's on.
#Colors are in RGB format.
def showMeTheColor(colors = (0,0,0)):
    #We're going to use this to change the color of the neoPixelStrip
    pixels.fill(colors)

def remapColors(val):
    #1643 was the max value noticed while running the potChecker
	 newColor = int(0+(255-0)*((val-0)/(1643-0)))
	 print("got Here")
	 print(newColor)
	 return newColor

while True:
    #First thing is get the values of the knobs themselves
    redKnoby = channel[0].value
    blueKnoby = channel[1].value
    greenKnoby = channel[2].value
    print(redKnoby)
    #Remaping the colors to a normal 0 -> 255 values
    redColor = remapColors(redKnoby)
    blueColor = remapColors(blueKnoby)
    greenColor = remapColors(greenKnoby)
    print("new color")
    print(redColor)
    showMeTheColor((redColor, greenColor, blueColor))
