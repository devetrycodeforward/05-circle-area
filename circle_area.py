# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.

import math 

def area_of_circle(r):
    area = (r ** 2)*(math.pi)
    return area

radius = int(input("What is the radius of the circle?")) 
result = area_of_circle(radius)
print ("The area of the circle is ", result)
