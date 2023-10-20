# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:14:16 2023

@author: niket
"""


import numpy as np
import math

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

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        elif -0.5 < f_m_n < 0.5:
            print("Found approximate solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

def bisection(f,a,b,N):
# Check if a and b bound a root
    if f(a)*f(b) >= 0:
        print("a and b do not bound a root")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

        
L =1
W =2
D =2
M =3
gamma = np.pi/3
a = newton_raphson(L, D, W, gamma)
print(f"Alpha in radians: {a}")

alpha_initial = 0
alpha = alpha_initial
f = lambda alpha: equation(alpha, L, D, W, gamma) 
solution = secant(f,0,2,25)
print(solution)


approx_phi = bisection(f,-1,2,100)
print(approx_phi)