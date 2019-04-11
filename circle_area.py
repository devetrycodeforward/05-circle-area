# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.

# Below are some tests which can give you an indication that your code seems to be correct.
import math
from test import testEqual

def area_of_circle(r):
    result = math.pi*(r**2)
    return result

t = area_of_circle(0)
testEqual(t, 0)
t = area_of_circle(1)
testEqual(t,math.pi)
t = area_of_circle(100)
testEqual(t, 31415.926535897932)
t = area_of_circle(-1)
testEqual(t, math.pi)
t = area_of_circle(-5)
testEqual(t, 25 * math.pi)
t = area_of_circle(2.3)
testEqual(t, 16.61902513749)
