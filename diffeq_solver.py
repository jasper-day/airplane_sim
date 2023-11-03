# Differential equation solver
# Input: System equation, initial conditions, forcing term
# Output: Array of integrated state variables through time
# Method: Runge-Kutta

import numpy as np

def rk_integrate(f, U_0, X, t):
    # Write code that integrates U through the time
    """
    Given initial conditions U_0 (state array), and an array of time values,
    returns an array with the state at each time value [U_0, U_1, ... U_n]
    Input:
    U_0: 1-dimensional array of initial conditions
    X: 2-dimensional array of commands across time
    f: function such that dU_dt = f(U, X, t)
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
        U[i+1] = rk4_step(f,U[i],X[i],t[i],dt[i])
    return U

def rk4_generator(U_0, f, dt):
    # might be useful for some real-time simulations?
    # I think that we have to put in better control options than having f explicitly depend on time, if we want real-time control.
    # Not sure how to incorporate live commands, 
    # and honestly I think that a generator isn't really the way to go here for this situation, but it might be useful for testing
    """
    Given initial conditions U_0 and a timestep dt, returns a generator (iterator) of future conditions.
    Input:
    U_0: Array of initial conditions
    f: function such that dU_dt = f(U, t)
    dt: desired timestep
    Output:
    Iterator that continually returns the next state of the system
    """
    # Initial conditions
    t = 0
    U_curr = U_0
    while True:
        yield U_curr
        # Take one step forward in time
        t += dt
        U_next = rk4_step(f, U_curr, [0,0], t, dt)
        U_curr = U_next


def rk4_step(f, U_n, X_n, t, dt):
    # RK4 algorithm (programming for computations, p. 254)
    # We have dU_dt = f(U, t) as our differential equation
    # We want to find U_n_1
    """
    Given: 
    U_n (state array)
    X_n (array of commands)
    f such that DU_dt = f(U, X, t)
    t: current time
    dt: desired time step
    Returns:
    Next value of U (state array)
    """
    f_n = f(U_n, X_n, t)
    # Forward Euler
    U_hat_midpoint = U_n + 1/2 * dt * f_n
    f_hat_midpoint = f(U_hat_midpoint, X_n, t + 1/2 * dt)
    # Backward Euler
    U_twiddle_midpoint = U_n + 1/2 * dt * f_hat_midpoint
    f_twiddle_midpoint = f(U_twiddle_midpoint, X_n, t + 1/2 * dt)
    # Crank-nicolson
    U_bar_n_1 = U_n + dt * f_hat_midpoint
    f_bar_n_1 = f(U_bar_n_1, X_n, t + dt)
    # Simpson's rule
    return U_n + dt/6 * (f_n + 2 * f_hat_midpoint + 2 * f_twiddle_midpoint + f_bar_n_1)

if __name__=="__main__":
    # test with simple harmonic oscillator
    def f(U, _X, _t):
        return np.array([U[1], -U[0]])
    U_0 = np.array([1,0])
    t = np.linspace(0, 10, 100)
    X = np.zeros_like(t)
    U = rk_integrate(f, U_0, X, t)
    import matplotlib.pyplot as plt
    plt.plot(t, U)
    plt.show()