#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:25:58 2023

@author: xavieryee
"""
import numpy as np
def _delta_E(alpha):
    return - (C_M_0 + C_M_alpha * alpha) / C_M_delta_E

def _C_L(alpha):
    return find_C_L(alpha, _delta_E(alpha))

def _C_D(alpha):
    return find_C_D(_C_L(alpha))

def _C_M(alpha):
    return find_C_M(alpha, _delta_E(alpha))


L = find_lift(V, _C_L(alpha))
D = find_drag(V, _C_D(alpha)) 
W = find_weight()

def equation (alpha,L,D,W,gamma):
    term_1 = find_lift(V, _C_L(alpha)) * np.cos(alpha)
    term_2 = find_drag(V, _C_D(alpha)) * np.sin(alpha)
    term_3 = find_weight() * np.cos(alpha+gamma)
    return term_1 + term_2 + term_3


def derivative (alpha,L,D,W,gamma):
    term_1 = find_lift(V, _C_L(alpha)) * np.sin(alpha)
    term_2 = - find_drag(V, _C_D(alpha)) * np.cos(alpha)
    term_3 = find_weight() * np.sin(alpha+gamma)
    return term_1 + term_2 + term_3

def newton_raphson(L, D , W , gamma , alpha_initial=0.0, max_interations=1000, tol=1e-6):
    alpha = alpha_initial
    for i in range (max_interations):
        f_alpha_alpha = equation(alpha, L, D, W, gamma)
        f_prime_alpha = derivative(alpha, L, D, W, gamma)
        alpha_new = alpha - f_alpha_alpha / f_prime_alpha
        
        
        if abs(alpha_new - alpha) < tol:
            return alpha_new
        

gamma = np.pi/3

a = newton_raphson(L, D, W, gamma)
print(f"Alpha in radians: {a}")



