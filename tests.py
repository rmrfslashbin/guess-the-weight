#!/usr/bin/env python

from z3 import *


def test_range(weights, upper, lower):
    # Define the plates
    a, b, c, d, e, q = Ints('a b c d e q')

    # Create a solver
    s = Solver()
    s.add(
        q == 1,  # One and only one bar
        a <= weights["a"]["qty"], a >= 0, a % 2 == 0,  # 0 or more plates, must be in pairs
        b <= weights["b"]["qty"], b >= 0, b % 2 == 0,
        c <= weights["c"]["qty"], c >= 0, c % 2 == 0,
        d <= weights["d"]["qty"], d >= 0, d % 2 == 0,
        e <= weights["e"]["qty"], e >= 0, e % 2 == 0,
        weights["a"]["wght"] * a + weights["b"]["wght"] * b + weights["c"]["wght"] * c + weights["d"]["wght"] * \
            d + weights["e"]["wght"] * e + weights["q"]["wght"] * \
        q > lower,  # must be at least
        weights["a"]["wght"] * a + weights["b"]["wght"] * b + weights["c"]["wght"] * c + weights["d"]["wght"] * d + weights["e"]["wght"] * e + weights["q"]["wght"] * q < upper)  # can't be more than
    
    # Check to see if the plan is sane
    z = s.check()
    if z.r != 1:
        return False
    else:
        return s

