import math
'''
calculate_circle_are return the area of a circle has one parameter that is the radius of the circle in order to work
'''
def calculate_circle_area(radius):
    area = math.pi * (radius**2)
    return float(area)
'''
calculate_sphere_volume return the volume of a sphere has one parameter that is the radius in order to work
'''
def calculate_sphere_volume(radius):
    volume = 4/3*math.pi*(radius**3)
    return float(volume)
'''
calculate_bmi return the bmi of a person doesn't require parameteres but require to fill up some inputs height and weight
'''
def calculate_bmi():
    weight = float(input("Enter your weight in Kilograms: "))
    height = float(input("Enter your height in centimeres: "))
    bmi= weight/(height**2)
    return bmi
'''
calculate_hypotenuse return the hypotenuse from a triangle no parameters but require to fill up some inputs A and B side of a triangle
'''
def calculate_hypotenuse():
    a = float(input("Insert length of A side of the triangle: "))
    b = float(input("Insert length of B side of the triangle: "))
    return math.hypot(a,b)



