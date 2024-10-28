def power(x, n):
    return x ** n

def sqrt(x):
    return x ** 0.5

def n_root(x, n):
    return x ** (1 / n)
    
def factorial(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result