import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def log(a, b):
    if a <= 0:
        raise ValueError("a must be positive")
    if b <= 0 or b == 1:
        raise ValueError("b must be positive and not equal to 1")
    return math.log(a, b)

def exp(a, b):
    return a ** b



import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply (a, b):
    a * b


def logarithm(a, b):
    if b <= 0 or a <=0 or b == 1:
        raise ValueError("Cannot take log of 0")
    return math.log(a, b)

def exponent(a, b):
     return a ** b

