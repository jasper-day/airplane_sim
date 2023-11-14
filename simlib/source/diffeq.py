# Differential equation solver
# Input: System equation, initial conditions, forcing term
# Output: Array of integrated state variables through time
# Method: Runge-Kutta

import numpy as np
import inspect

def rk4_integrate(f, U_0, X, t):
    # Write code that integrates U through the time
    """
    Given initial conditions U_0 (state array), and an array of time values,
    returns an array with the state at each time value [U_0, U_1, ... U_n]
    Input:
    f: function such that dU_dt = f(U, X, t)
    U_0: 1-dimensional array of initial conditions
    X: 2-dimensional array of commands across time
    t: 1-dimensional array of time values
    Output:
    U: 2-dimensional array of state at each moment in time
    """
    # find time differences
    dt = np.diff(t)
    # create an empty array for the state array
    U = np.empty([len(t),len(U_0)])
    U[0] = U_0 # fill in with initial conditions given by root finding
    # loop rk4_step for every time value
    for i in range(len(dt)):
        if inspect.isfunction(X):
            U[i + 1] = rk4_step(f, U[i], X, t[i], dt[i])
        else:
            U[i+1] = rk4_step(f,U[i],X[i],t[i],dt[i])
    return U

def rk4_step(f, U_n, X_n, t, dt):
    # RK4 algorithm (programming for computations, p. 254)
    # We have dU_dt = f(U, t) as our differential equation
    # We want to find U_n_1
    """ Take one step forward in time via runge-kutta 4 integration
    Given: 
    U_n (state array)
    X_n (array of commands)
    f such that DU_dt = f(t, U, X)
    t: current time
    dt: desired time step
    Returns:
    Next value of U (state array)
    """
    f_n = f(t, U_n, X_n)
    # Forward Euler
    U_hat_midpoint = U_n + 1/2 * dt * f_n
    f_hat_midpoint = f(t + 1/2 * dt, U_hat_midpoint, X_n)
    # Backward Euler
    U_twiddle_midpoint = U_n + 1/2 * dt * f_hat_midpoint
    f_twiddle_midpoint = f(t + 1/2 * dt, U_twiddle_midpoint, X_n)
    # Crank-nicolson
    U_bar_n_1 = U_n + dt * f_hat_midpoint
    f_bar_n_1 = f(t + dt, U_bar_n_1, X_n)
    # Simpson's rule
    return U_n + dt/6 * (f_n + 2 * f_hat_midpoint + 2 * f_twiddle_midpoint + f_bar_n_1)

if __name__=="__main__":
    # test with simple harmonic oscillator
    def dU_dt(_t, U, _X,):
        # x'' = -x
        # x' = U[1]
        # x = U[0]
        return np.array([U[1], -U[0]])
    U_0 = np.array([1,0])
    t = np.linspace(0, 2*np.pi, 100)
    X = lambda t: None
    U = rk4_integrate(dU_dt, U_0, X, t)
    import matplotlib.pyplot as plt
    plt.plot(t, U)
    plt.show()