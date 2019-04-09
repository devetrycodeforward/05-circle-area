import math
from circle_area import area_of_circle

def test_zero_radius():
    assert area_of_circle(0) == 0

def test_one_radius():
    assert area_of_circle(1) == math.pi

def test_100_radius():
    assert area_of_circle(100) == 31415.926535897932

def test_negative_one_radius():
    assert area_of_circle(-1) == math.pi

def test_negative_five_radius():
    assert area_of_circle(-5) == math.pi * 25

def test_two_point_three_radius():
    assert area_of_circle(2.3) == 16.619025137490002