from math import sin

defaultA = 5
defaultB = 2
defaultC = 8

def trianglePerimeter(a, b, c):
    if a == None:
        a = defaultA
    if b == None:
        b = defaultB
    if c == None:
        c = defaultC
    return a+b+c

def triangleArea(a, b, c):
    if a == None:
        a = defaultA
    if b == None:
        b = defaultB
    if c == None:
        c = defaultC
    return a*b*sin(c)*0.5