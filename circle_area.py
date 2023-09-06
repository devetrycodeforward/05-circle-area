import math

def area_of_circle(r):       # define a function called area_of_circle which takes an argument called r
    area = (r**2) * math.pi  # area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....
    #print(area)             # self test pt 1
    return area              # return the area of a circle whose radius is r

#area_of_circle(2)           # self test pt 2
