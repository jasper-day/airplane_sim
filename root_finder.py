# Functional root finder
# Input: function of multiple variables, starting point
# Output: Roots of that function
# Method: Newton's method of some kind

from airplane_dynamics import find_lift, find_drag, find_moment, find_weight, \
    find_C_L, find_C_D, find_C_M
from vehicle import C_M_0, C_M_alpha, C_M_delta_E
import math

# Functions prefixed with _ (underscore) are *private functions* 
# not intended to be called outside of this module. We use them
# as intermediate results in calculating the lift, drag, and moment
# at equilibrium given alpha.

def _delta_E(alpha):
    return - (C_M_0 + C_M_alpha * alpha) / C_M_delta_E

def _C_L(alpha):
    return find_C_L(alpha, _delta_E(alpha))

def _C_D(alpha):
    return find_C_D(_C_L(alpha))

def _C_M(alpha):
    return find_C_M(alpha, _delta_E(alpha))

def minimizing_function(V, gamma):
    "Returns a function of alpha which should be minimized for trim conditions"
    W = find_weight()
    def f(alpha):
        L = find_lift(V, _C_L(alpha))
        D = find_drag(V, _C_D(alpha))
        M = find_moment(V, _C_M(alpha))
        return -L*math.cos(alpha) - D*math.sin(alpha) + W*math.cos(alpha + gamma)
    return f

# use any root-finding code here to find the root of f(alpha)
# The following is an example, but we can do better lol
from scipy import optimize

_f = minimizing_function(100, 5)
print(optimize.newton(_f, 0))

