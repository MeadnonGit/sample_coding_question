#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:21:11 2020

@author: arousal
"""

import math as m

def maxi_diff(vec):
    """
    Return the difference between the maximum and the minimum of a numerical
    vector vec. The vector is not ordered and, the minimum and maximum are not
    explicitly determined.
    
    Parameter
    ---------
    vec : list, sequence of numeric values
    
    Example
    -------
    maxi_diff([100,70,1000,0]) = 1000
    
    """
    
    # Initialisation of the differences between first element of vec and its
    # lower and upper bounds
    min_diff, max_diff = 0, 0
    
    for value in vec:
        if (vec[0] - value) > min_diff:
            min_diff = vec[0] - value
        if (vec[0] - value) < max_diff:
            max_diff = vec[0] - value
    
    return m.fabs(min_diff) + m.fabs(max_diff)

# Test
u = [100, 70, 0, 1000, 2]
print("maximal difference in {} is {}".format(u, maxi_diff(u)))
    
    