# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:14:16 2023

@author: niket
"""


import numpy as np
import math
from aero_analytical_build_ToBeCompleted import CM_0, CM_alpha,CM_delta


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
    

#function to calculate the root using secant
def secant(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

        Parameters
        ----------
        f : function
            The function for wherein we are trying to approximate a solution f(x)=0.
        a,b : numbers
            The interval in which to search for a solution.
        N : (positive) integer
            The number of iterations to carry out.

        Returns
        -------
        m_N : number
            The x intercept of the secant line on the the Nth interval
                m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
            The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
            for some intercept m_n then the function returns this solution.
            If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
            iterations, the secant method fails and return None.
        #condition where secant method fails'''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    #defining variables
    a_n = a
    b_n = b
    m_n_old=0
    #for loop to iterate the secant process for the number of iterations specified
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        ea = abs((m_n - m_n_old )/(m_n))
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
            m_n_old = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
            m_n_old = m_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        elif -0.5 < f_m_n < 0.5:
            print("Found approximate solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n)), ea

def bisection(f,a,b,N):
        '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

        Parameters
        ----------
        f : function
            The function for which we are trying to approximate a solution f(x)=0.
        a,b : numbers
            The interval in which to search for a solution. The function returns
            None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        N : (positive) integer
            The number of iterations to implement.

        Returns
        -------
        m_N : number
            The estimate of the root determined by:
                m_n = (a_n + b_n)/2
                where a_n is the lower bound, and b_n is the higher bound.
            The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
            for some intercept m_n then the function returns this solution.
            If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
            iterations, the bisection method fails and return None. '''
# Check if a and b bound a root
        ea = 0
        if f(a)*f(b) >= 0:
            print("a and b do not bound a root")
            return None
        a_n = a
        b_n = b
        m_n_old=0

        for n in range(1,N+1):
            m_n = (a_n + b_n)/2
            ea = abs((m_n - m_n_old )/(m_n))
            f_m_n = f(m_n)
            if f(a_n)*f_m_n < 0:
                a_n = a_n
                b_n = m_n
                m_n_old = m_n
            elif f(b_n)*f_m_n < 0:
                a_n = m_n
                b_n = b_n
                m_n_old = m_n
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Bisection method fails.")
                return None
        return (a_n + b_n)/2, ea

        
#defining velocity and gamma
V = 100
gamma = 5

#newton raphson from scipy
from root_finder import minimizing_function
f = minimizing_function(V, gamma)

#secant method
solution,error_s = secant(f,-1,2,25)
#output the solution and error of the secant method in decimal
print(solution,error_s)

#bisection method
approx_phi,error_b = bisection(f,-1,2,100)
#output the solution and error of the bisection method in decimal
print(approx_phi,error_b)


alpha_initial = 0
alpha = alpha_initial
f = lambda alpha: equation(alpha, L, D, W, gamma) 
L =1
W =2
D =2
M =3
gamma = np.pi/3
a = newton_raphson(L, D, W, gamma)
print(f"Alpha in radians: {a}")

#choosing the best value for alpha
actual_alpha = approx_phi 
#finding delta_e
delta_e = -(CM_0 + CM_alpha*actual_alpha)/CM_delta
print(delta_e)
