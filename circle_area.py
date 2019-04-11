# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.
import math

def area_of_circle(r):
    a = (math.pi * math.pow(r, 2))
    return a

def main():
    t = 0
    result = area_of_circle(t)
    print("The area of a circle with radius", t, "is", result)
         
if __name__ == "__main__":
    main()
