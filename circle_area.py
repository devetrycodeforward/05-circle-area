# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
import math
def area_of_circle(r):
    area = (r ** 2) * math.pi
    return area

def main():
  circle = area_of_circle(2.3)
  print(circle)

main()
# HINT: You'll need to import math to solve this problem correctly.
