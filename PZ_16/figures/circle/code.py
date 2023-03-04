from math import pi

defaulRadius = 5

def circlePerimeter(radius):
    if radius == None:
        radius = defaulRadius
    return radius*2 * pi

def circleArea(radius):
    if radius == None:
        radius = defaulRadius
    return radius**2 * pi