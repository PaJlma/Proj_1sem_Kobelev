defaulRadius = 5
PI = 3.1415926535

def circlePerimeter(radius):
    if radius == None:
        radius = defaulRadius
    return radius*2 * PI

def circleArea(radius):
    if radius == None:
        radius = defaulRadius
    return radius**2 * PI