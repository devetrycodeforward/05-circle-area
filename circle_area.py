# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.
import math
pi = math.pi
r = float (input("The radius of the circle is:"))
def area_of_circle(r):
    area = pi* r**2
    return area
print ("The area of a circle with radius", r, "is", area_of_circle(r))
