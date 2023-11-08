#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:25:58 2023

@author: xavieryee
"""
'''
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


def derivative (alpha,L,D,W,gamma):
    term_1 = find_lift(V, _C_L(alpha)) * np.sin(alpha)
    term_2 = - find_drag(V, _C_D(alpha)) * np.cos(alpha)
    term_3 = find_weight() * np.sin(alpha+gamma)
    return term_1 + term_2 + term_3

def newton_raphson(alpha, alpha_initial=0.0, max_interations=1000, tol=1e-6):
    alpha = alpha_initial
    for i in range (max_interations):
       
        alpha_new = alpha - f(alpha) / f_derivative
        
        
        if abs(alpha_new - alpha) < tol:
            return alpha_new
        
print(newton_raphson(alpha, alpha_initial=0.0, max_interations=1000, tol=1e-6))



from scipy import optimize

V = 100
gamma = 5

_f = minimizing_function(V,gamma)
print(optimize.newton(_f, 0))

# a = newton_raphson(L, D, W, gamma)
# print(f"Alpha in radians: {a}")'''



# python files with the aerodynamics coefficients 
# at discrete values of the angle of attack alpha and 
# elevator angle delta_el

# importing modules
import numpy as np
import math

from aero_table import CD, CL, CM, CL_el, CM_el, alpha, delta_el

alpha = np.array([-16, -12, -8, -4, -2, 0, 2, 4, 8, 12]) * np.pi / 180
delta_el = np.array([-20, -10, 0, 10, 20]) * np.pi / 180

# solve by np.polyfit
CL_alpha, CL_0 = np.polyfit(alpha, CL, 1)
CL_delta_E, _ = np.polyfit(delta_el, CL_el, 1)
CM_alpha, CM_0 = np.polyfit(alpha, CM, 1)
CM_delta_E, _ = np.polyfit(delta_el, CM_el, 1)
CL = CL  # CL_el almost 0
K, _, CD_0 = np.polyfit(CL, CD, 2)

if __name__ == '__main__':
    print("CL_aplha, CL_0: {}, {}".format(CL_alpha, CL_0))
    print("CL_delta_E: {}".format(CL_delta_E))
    print("CM_aplha, CM_0: {}, {}".format(CM_alpha, CM_0))
    print("CM_delta_E: {}".format(CM_delta_E))
    print("K, CD_0: {}, {}".format(K, CD_0))
