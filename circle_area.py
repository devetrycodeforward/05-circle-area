def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False
           
# Below is a set of tests so you can check if your code is correct.
from test import testEqual


testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
