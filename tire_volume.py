import math
from datetime import datetime

def calc_volume(width, aspect_ratio, diameter):
    return (math.pi * width ** 2 * aspect_ratio*(width * aspect_ratio + 2540 * diameter))/10000000000
    

width = float(input("Enter the tire width in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio o the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = calc_volume(width, aspect_ratio, diameter)
print(f"The approximate volume is {round(volume, 2)} liters")

date = datetime.now()

with open("volumes.txt", "a") as v:
    v.write(f"{date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}\n")