# added tire prices and store users phone number if they want to purchase the tires

import math
from datetime import datetime

def calc_volume(width, aspect_ratio, diameter):
    return (math.pi * width ** 2 * aspect_ratio*(width * aspect_ratio + 2540 * diameter))/10000000000
    

width = float(input("Enter the tire width in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio o the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = calc_volume(width, aspect_ratio, diameter)
print(f"The approximate volume is {round(volume, 2)} liters")

price = 0
purchase = False

if width == 185 and aspect_ratio == 55 and diameter == 14:
    price = 85
elif width == 195 and aspect_ratio == 65 and diameter == 15:
    price = 95
elif width == 205 and aspect_ratio == 60 and diameter == 16:
    price = 110
elif width == 215 and aspect_ratio == 60 and diameter == 16:
    price = 120
elif width == 225 and aspect_ratio == 65 and diameter == 17:
    price = 145
elif width == 235 and aspect_ratio == 60 and diameter == 18:
    price = 165

if price == 0:
    print("Prices of tires with those dimensions are NOT available.")
else:
    print(f"Available tires with those dimensions are ${price} each.")
    purchase = input("Would you like to purchase these tires? (Y/N) ").lower() == "y"

phone_number = ""
if purchase:
    phone_number = input("Please enter your phone number: ")

date = datetime.now()

with open("volumes.txt", "a") as v:
    if purchase: 
        v.write(f"{date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number}\n")
    else:
        v.write(f"{date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}\n")