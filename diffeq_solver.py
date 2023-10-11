# Differential equation solver
# Input: System equation, initial conditions, forcing term
# Output: Array of integrated state variables through time
# Method: Runge-Kutta

import math 

def rk_integrate(U_0, f, t):
    # Write code that integrates U through the time
    #create an array from 0 to 100s in time step of 0.1 
    #iterates rk4 step
    """
    Given initial conditions U_0 (state array), and an array of time values,
    returns an array with the state at each time value [U_0, U_1, ... U_n]
    """
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
