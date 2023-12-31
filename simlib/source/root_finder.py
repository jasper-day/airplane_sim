# Functional root finder
# Input: function of multiple variables, starting point
# Output: Roots of that function
# Method: Newton's method of some kind

from dynamics import find_lift, find_drag, find_moment, find_weight, \
    find_C_L, find_C_D, find_C_M
from curve_fit import C_M_0, C_M_alpha, C_M_delta_el
import math
import numpy as np
import matplotlib.pyplot as plt


# Functions prefixed with _ (underscore) are *private functions* 
# not intended to be called outside of this module. We use them
# as intermediate results in calculating the lift, drag, and moment
# at equilibrium given alpha.

def find_delta_el(alpha):
    return - (C_M_0 + C_M_alpha * alpha) / C_M_delta_el

def _C_L(alpha):
    return find_C_L(alpha, find_delta_el(alpha))

def _C_D(alpha):
    return find_C_D(_C_L(alpha))

def _C_M(alpha):
    return find_C_M(alpha, find_delta_el(alpha))


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


def bisection(f,a,b,N):
        '''Approximate solution of f(x)=0 on interval [a,b] by the bisection method.

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
        (a_n + b_n)/2 : number
            The estimate of the root determined by:
                (a_n + b_n)/2
                where a_n is the lower bound, and b_n is the higher bound.
            The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
            for some intercept m_n then the function returns this solution.
            If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
            iterations, the bisection method fails and return None. '''
        ea = 0
        # Check if a and b bound a root
        if f(a)*f(b) >= 0:
            raise ValueError("a and b do not bound a root")
        a_n = a
        b_n = b
        m_n_old=0

        for n in range(1,N+1):
            m_n = (a_n + b_n)/2
            #calculate approximate error of the root found
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
                return {"solution": m_n, "success": True, "error": 0}
            else:
                return {"solution": None, "success": False, "error": math.huge}
        return {"solution": (a_n + b_n)/2, "success": True, "error": ea}

def find_system(V, gamma):
    """Given velocity and flight path angle, calculates the angle of attack
    Output:
    {'alpha': angle of attack
     'delta_el': elevator inclination
     'Thrust': Thrust force
     'V': Airspeed
     'gamma': flight path angle
     'pitch': pitch angle}"""
    f = minimizing_function(V, gamma)
    res = bisection(f, -math.pi/2 + 0.1, math.pi/2, 1000)
    alpha = res["solution"] if res["success"] else None
    system = get_system_parameters(V, gamma, alpha)
    system["alpha_error"] = res["error"]
    return system

def get_system_parameters(V, gamma, alpha):
    L = find_lift(V, _C_L(alpha))
    D = find_drag(V, _C_D(alpha))
    W = find_weight()
    T = D * math.cos(alpha) + W * math.sin(alpha + gamma) - L * math.sin(alpha)
    delta_el = find_delta_el(alpha)
    return {
        "alpha": alpha, 
        "delta_el": delta_el, 
        "Thrust": T, 
        "V": V, 
        "gamma": gamma,
        "pitch": alpha + gamma, 
    }



def plot_thrust_vs_velocity(ax, gamma_values, V_range):
    """Plots a graph for the thrust vs velocity for a range of velocities
      and flight path angles"""
    thrust_values = []
    alpha_values = [] 
    for gamma in gamma_values:
        thrust_data = []
        alpha_data = []
        for V in V_range:
            result = find_system(V, gamma)
            if -0.27925 < result["alpha"] < 0.2094395 :
                thrust_data.append(result["Thrust"])
        thrust_values.append(thrust_data)

    for i, gamma in enumerate(gamma_values):
        plt.subplot(121)
        plt.plot(V_range, thrust_values[i], label=f'Gamma = {gamma}')
    
    ax.set_xlabel('Velocity (V)')
    ax.set_ylabel('Thrust')
    ax.legend()
    ax.set_title('Thrust vs. Velocity for Different Gamma Values')
    ax.grid(True)

def plot_delta_el_vs_velocity(ax, gamma_values, V_range):
    """Plots a graph for the elevator angle vs velocity for a range of velocities
      and flight path angles"""
    delta_el_values = []
    for gamma in gamma_values:
        delta_el_data = []
        for V in V_range:
            result = find_system(V, gamma)
            if -0.27925 < result["alpha"] < 0.2094395 :
                delta_el_data.append(result["delta_el"])
        delta_el_values.append(delta_el_data)

    for i, gamma in enumerate(gamma_values):
        plt.subplot(122)
        plt.plot(V_range, delta_el_values[i], label=f'Gamma = {gamma}')
  

    ax.set_xlabel('Velocity (V)')
    ax.set_ylabel('Elevator Deflection (rad)')
    ax.legend()
    ax.set_title('Elevator Deflection vs. Velocity for Different Gamma Values')
    ax.grid(True)
    
    

if __name__ == "__main__":
    from pprint import pprint
    pprint(find_system(100, 0.05))

    #definine the range of velocities and flight path angles that need to be plotted
    V_range = np.linspace(75, 150, 400)
    gamma_values = np.linspace(0, 1, 11)

    #outputs both of the plots in the same figure
    fig, axs = plt.subplots(2)
    plot_thrust_vs_velocity(axs[0], gamma_values, V_range)  # Add this line to plot thrust vs. velocity
    plot_delta_el_vs_velocity(axs[1], gamma_values, V_range)
    plt.show()