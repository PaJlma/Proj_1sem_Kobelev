__all__ = ['trianglePerimeter', 'triangleArea']

from math import sin

defaultA = 5
defaultB = 2
defaultC = 8

def trianglePerimeter(a=defaultA, b=defaultB, c=defaultC):
    if a == None:
        a = defaultA
    if b == None:
        b = defaultB
    if c == None:
        c = defaultC
    return a+b+c

def triangleArea(a=defaultA, b=defaultB, c=defaultC):
    return a*b*sin(c)*0.5