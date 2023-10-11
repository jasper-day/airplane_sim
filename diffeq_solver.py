# Differential equation solver
# Input: System equation, initial conditions, forcing term
# Output: Array of integrated state variables through time
# Method: Runge-Kutta

import math 
import numpy as np
def rk_integrate(U_0, f, t):
    # Write code that integrates U through the time
    """
    Given initial conditions U_0 (state array), and an array of time values,
    returns an array with the state at each time value [U_0, U_1, ... U_n]
    """
    #time step size
    dt = 0.1
    #create an array for the time in tervals of 0.1 from 0s to 100s
    t = np.linspace(0, 100, (100/dt)+1)
    #create an empty array for the state array
    U = np.empty([100,6])
    U[0] = [0,0,0,0,0,0] #fill in with initial conditions given by root finding
    #loop rk4_step for every time value
    for i in range (0,100):
        U[i+1] = rk4_step(U[i],f,t[i],dt)
    pass


def rk4_step(U_n, f, t, dt):
    # RK4 algorithm (programming for computations, p. 254)
    # We have dU_dt = f(U, t) as our differential equation
    # We want to find U_n_1
    """
    Given: U_n (state array)
    f such that DU_dt = f(U, t)
    t: current time
    dt: desired time step
    
    Returns:
    Next value of U (state array)
    """
    f_n = f(U_n, t)
    # Forward Euler
    U_hat_midpoint = U_n + 1/2 * dt * f_n
    f_hat_midpoint = f(U_hat_midpoint, t + 1/2 * dt)
    # Backward Euler
    U_twiddle_midpoint = U_n + 1/2 * dt * f_hat_midpoint
    f_twiddle_midpoint = f(U_twiddle_midpoint, t + 1/2 * dt)
    # Crank-nicolson
    U_bar_n_1 = U_n + dt * f_hat_midpoint
    f_bar_n_1 = f(U_bar_n_1, t + dt)
    # Simpson's rule
    return dt/6 * (f_n + 2 * f_hat_midpoint + 2 * f_twiddle_midpoint + f_bar_n_1)

