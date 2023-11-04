#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:25:58 2023

@author: xavieryee
"""
from airplane_dynamics import find_lift, find_drag, find_moment, find_weight, \
      find_C_L, find_C_D, find_C_M
from curve_fit import C_M_0, C_M_alpha, C_M_delta_el
import math
import numpy as np
from sympy import symbols, diff



def _delta_E(alpha):
    return - (C_M_0 + C_M_alpha * alpha) / C_M_delta_el


def _C_L(alpha):
    return find_C_L(alpha, _delta_E(alpha))

def _C_D(alpha):
    return find_C_D(_C_L(alpha))

def _C_M(alpha):
    return find_C_M(alpha, _delta_E(alpha))
def minimizing_function(V, gamma):

    """
    Returns a function of alpha which should be minimized for trim conditions

    Input:
    V: Velocity (m/s)
    gamma: flight angle (rad)

    Output:
    f: function of alpha
    """
    W = find_weight()

    def f(alpha):
        L = find_lift(V, _C_L(alpha))
        D = find_drag(V, _C_D(alpha))
        M = find_moment(V, _C_M(alpha))
        return -L*math.cos(alpha) - D*math.sin(alpha) + W*math.cos(alpha + gamma)
    return f


W = find_weight()

from sympy import symbols, diff
import math

# ...

# Define the variables and the function 'f'
alpha = symbols('alpha')
V = 100  # Example value, replace with your actual value
gamma = 5  # Example value, replace with your actual value

def f(alpha):
    L = find_lift(V, _C_L(alpha))
    D = find_drag(V, _C_D(alpha))
    return -L*math.cos(alpha) - D*math.sin(alpha) + W*math.cos(alpha + gamma)

# Find the first derivative of 'f' with respect to 'alpha'
f_derivative = diff(f(alpha), alpha)

# Print the derivative of 'f'
print("The first derivative of the function f is: ", f_derivative)


'''def derivative (alpha,L,D,W,gamma):
    term_1 = find_lift(V, _C_L(alpha)) * np.sin(alpha)
    term_2 = - find_drag(V, _C_D(alpha)) * np.cos(alpha)
    term_3 = find_weight() * np.sin(alpha+gamma)
    return term_1 + term_2 + term_3'''

def newton_raphson(alpha, alpha_initial=0.0, max_interations=1000, tol=1e-6):
    alpha = alpha_initial
    for i in range (max_interations):
       
        alpha_new = alpha - f(alpha) / f_derivative
        
        
        if abs(alpha_new - alpha) < tol:
            return alpha_new
        
print(newton_raphson(alpha, alpha_initial=0.0, max_interations=1000, tol=1e-6))



'''from scipy import optimize

V = 100
gamma = 5

_f = minimizing_function(V,gamma)
print(optimize.newton(_f, 0))

# a = newton_raphson(L, D, W, gamma)
# print(f"Alpha in radians: {a}")'''



