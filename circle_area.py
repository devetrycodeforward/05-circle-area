# TODO: DEFINE a function using the def keyword called `area_of_circle`
# TODO: implement the function to RETURN (NOT PRINT) the area of a circle whose radius is r
# HINT: You'll need to import math to solve this problem correctly.
import math

def area_of_circle(r):
    answer = (math.pi * r**2)

    return(answer)

def main():
    area_of_circle(5)

if __name__ == "__main__":
    main()
