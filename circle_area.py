# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.

import math

def area_of_circle(r):
    result = math.pi*(r**2)
    return result

def main():                      # Define the main function
    print("circle area of radius 3 is ", area_of_circle(3))

main()   
