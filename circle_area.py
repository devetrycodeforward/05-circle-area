# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.
import math
pi = math.pi
def area_of_circle(r):
    area = pi* r**2
    return print(area)
r = float (input("The radius of the circle is:"))
area_of_circle(r)
