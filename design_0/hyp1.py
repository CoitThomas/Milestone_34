"""This module contains all the functions needed to successfully run
find_hypotenuse.py
"""

import math

def assert_and_convert(user_input):
    """assert_and_convert(unknown) -> float

    Assert that the input given by the user is appropriate. Convert
    that input into a float. Return the input.
    """
    assert (isinstance(user_input, float) or
            isinstance(user_input, int)), 'Value must be of type int or type float.'
    assert user_input > 0, 'Value should be greater than zero.'
    if isinstance(user_input, int):
        float(user_input)
    return user_input

def get_input():
    """get_input() -> (float, float)

    Instruct and gather user input of two sides of a right
    triangle.
    """
    print 'Enter the two sides of your right triangle.'
    input_a = input('a:')
    side_a = assert_and_convert(input_a)
    input_b = input('b:')
    side_b = assert_and_convert(input_b)
    return (side_a, side_b)

def find_hypotenuse(side_a, side_b):
    """find_hypotenuse(float, float) -> float

    Calculate and return the hypotenuse of a right triangle.
    """
    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
