# Functional root finder
# Input: function of multiple variables, starting point
# Output: Roots of that function
# Method: Newton's method of some kind

from airplane_dynamics import find_lift, find_drag, find_moment, find_weight, \
    find_C_L, find_C_D, find_C_M
from vehicle import C_M_0, C_M_alpha, C_M_delta_E
import math
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Disable Matplotlib interactive mode
plt.ioff()


# Functions prefixed with _ (underscore) are *private functions* 
# not intended to be called outside of this module. We use them
# as intermediate results in calculating the lift, drag, and moment
# at equilibrium given alpha.

def find_delta_E(alpha):
    return - (C_M_0 + C_M_alpha * alpha) / C_M_delta_E

def _C_L(alpha):
    return find_C_L(alpha, find_delta_E(alpha))

def _C_D(alpha):
    return find_C_D(_C_L(alpha))

def _C_M(alpha):
    return find_C_M(alpha, find_delta_E(alpha))


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


from Niketarootfinding import bisection

def find_system(V, gamma):
    f = minimizing_function(V, gamma)
    res = bisection(f, -math.pi/2 + 0.5, math.pi/2, 1000)
    alpha = res["solution"] if res["success"] else None
    L = find_lift(V, _C_L(alpha))
    D = find_drag(V, _C_D(alpha))
    W = find_weight()
    T = D * math.cos(alpha) + W * math.sin(alpha + gamma) - L * math.sin(alpha)
    delta_E = find_delta_E(alpha)
    return {"alpha": alpha, "delta_E": delta_E, "Thrust": T}
    

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
        #raise ValueError(f"Secant method fails: f({a}) = {f(a)} and f({b}) = {f(b)}")
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
            return {"solution": m_n, "success": True, "error": 0}
        # elif -0.5 < f_m_n < 0.5:
        # I don't think you want this
            # return {"solution": m_n, "success": True, "error": ea}
        # else:
            # print("Secant method fails.")
            # return None
    return {"solution": a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n)),"success": True, "error": ea}


if __name__ == "__main__":
    from pprint import pprint
    pprint(find_system(100, 0.05))

    V = 100
    gamma = 0.05

    f = minimizing_function(V, gamma)

    #secant method
    result_secant = secant(f,-1,2,25)
    #output the solution and error of the secant method in decimal
    from pprint import pprint
    pprint(result_secant)

#plot 3d graph to determine ranges of V and gamma
    v_p = np.linspace(0, 200, 400)
    gamma_p = np.linspace(-math.pi/2, math.pi/2, 400)
    params = [(v_p, gamma_p)]
    alpha_p = np.zeros((400, 400))
    for j in range(400):
        for i in range(400):
            f = minimizing_function(v_p[i], gamma_p[j])
            alpha_temp = secant(f,-1,2,25)
            if alpha_temp is not None:
                alpha_value = alpha_temp['solution']
                if -16*(np.pi/180) < alpha_value < 20*(np.pi/180):
                    alpha_p[i, j] = alpha_value
                    



    V_p, Gamma_p = np.meshgrid(v_p,gamma_p)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(V_p, Gamma_p, alpha_p, cmap='viridis')
    ax.set_xlabel('V')
    ax.set_ylabel('Gamma')
    ax.set_zlabel('Alpha')

    plt.show()
# plot alpha vs params for each parameter     