#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:25:58 2023

@author: xavieryee
"""
import numpy as np

def equation (alpha,L,D,W,gamma):
    term_1 = -L * np.cos(alpha)
    term_2 = -D * np.sin(alpha)
    term_3 = W * np.cos(alpha+gamma)
    return term_1 + term_2 + term_3


def derivative (alpha,L,D,W,gamma):
    term_1 = L * np.sin(alpha)
    term_2 = -D * np.cos(alpha)
    term_3 = -W * np.sin(alpha+gamma)
    return term_1 + term_2 + term_3

def newton_raphson(L, D , W , gamma , alpha_initial=0.0, max_interations=1000, tol=1e-6):
    alpha = alpha_initial
    for i in range (max_interations):
        f_alpha_alpha = equation(alpha, L, D, W, gamma)
        f_prime_alpha = derivative(alpha, L, D, W, gamma)
        alpha_new = alpha - f_alpha_alpha / f_prime_alpha
        
        
        if abs(alpha_new - alpha) < tol:
            return alpha_new
        
L =1
W =2
D =2
M =3
gamma = np.pi/3

a = newton_raphson(L, D, W, gamma)
print(f"Alpha in radians: {a}")