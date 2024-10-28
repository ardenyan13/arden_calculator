import math

def sin(theta):
    return math.sin(math.radians(theta))

def cos(theta):
    return math.cos(math.radians(theta))
        

def tan(theta):
    if abs(cos(theta)) < 1e-10:
        raise ZeroDivisionError("Can not divide by 0")
    return math.tan(math.radians(theta))