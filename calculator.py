"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot divide by number less than 0")
    return math.sqrt(a)

def hypotenuse (a, b):
    return math.hypot(a, b)



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply (a, b):
    a * b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")

def logarithm(a, b):
    if b <= 0 or a <=0 or b == 1:
        raise ValueError("Cannot take log of 0")
    return math.log(a, b)

def exponent(a, b):
     return a ** b