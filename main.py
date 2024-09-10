
# Assignment 2
# Class: Software Testing
# Professor: Esa Huiskonen
# Student: Dan Le
# Team : 4

def classify_triangle(a, b, c):
    
    # Check for non-numeric input
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Error: invalid input data value"

    # Check for invalid input: negative or zero values
    if a <= 0 or b <= 0 or c <= 0:
        return "Error: invalid input data value"

    # Check if the input sides can form a valid triangle using the triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return "Error: invalid input data value"

    # Determine triangle type
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"