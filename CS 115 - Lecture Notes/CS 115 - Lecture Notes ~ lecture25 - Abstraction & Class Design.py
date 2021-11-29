# Sid Bhatia
# CS115-C
# Lecture # - Abstraction & Class Design

# Abstraction for a POint Class

# * fields/attribute
# ** one dimension, x (__init__(self), self.x)
# * methods
# ** getter(s)/setter(s) (encapsulation)
# ** string methods (__repr__, __str__)
# ** basic arithmetics (equality, addition, difference)
# ** abs / distance

# Afterward, we'll exten this to 2D

# Point 2D

# * attributes
# ** additional dimension (self.y)

# * mehtods
# ** only new things: getter/setter
# ** most of the other methods from Point will need to be adjusted

import sys

class Point:
    def validate_param(value): # checks if coordinate is an integer or float
        return isinstance(value, int) or isinstance(value, float)
 
    def validate(self): # validates x-coordinate argument
        return Point.validate_param(self.x)

    def signal_validation_error(self): # error handling method
        sys.exit("Invalid point: " + str(self))

    def __init__(self, value = 0): # constructor with default argument
        self.x = value
        if not self.validate(): 
            self.signal_validation_error()

    def __str__(self):
        return 'x = ' + str(self.x)
    
    def get_x(self): # getter method for x-coordinate
        return self.x
    
    def set_x(self, value): # setter method for x-coordinate
        self.x = value
        if not self.validate():
            self.signal_validation_error()

    def __eq__(self, other):
        diff = self - other
        return diff.is_zero()
    
    def is_zero(self):
        return self.get_x() == 0
    
    def __sub__(self, other):
        # assuming 'other' is an instance of Point
        return self + (-other)
    
    def __neg__(self):
        neg_x = -1 * self.get_x()
        return Point(neg_x)
    
    def __add__(self, other):
        # assuming 'other' is an instance of Point
        new_x = self.get_x() + other.get_x()
        return Point(new_x)
    