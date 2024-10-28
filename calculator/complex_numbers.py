def add_complex(x, y):
    return complex(x) + complex(y)

def subtract_complex(x, y):
    return complex(x) - complex(y)

def multiply_complex(x, y):
    return complex(x) * complex(y)

def divide_complex(x, y):
    if y == 0:
        raise ZeroDivisionError("Can not divide by 0")
    return complex(x) / complex(y)