import math

print("NNPC Automation System")
print("----------------------------------------------")

radius = float(input("Enter the Radius of the Tank : "))
height = float(input("Enter the Height of the Tank : "))
vol = math.pi * (radius ** 2) * height

print(f"The Volume of the Oil in the Tank is :  {vol} Meter Cube")
