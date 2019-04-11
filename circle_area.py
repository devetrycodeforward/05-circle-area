import math

def area_of_circle(r):
    a = math.pi * r ** 2
    return a

radius = 25
result = area_of_circle(radius)
print("The area of a circle with radius", radius, "is", result)
