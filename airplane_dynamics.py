"""
Code for flight mechanics

Contains functions for calculating aerodynamic forces and moments, as well as
the equations of motion for the airplane.

All units should be normalized to SI units
All angles in radians
"""

import math

from env import gravity, air_density
from vehicle import Sref, cbar, acMass, inertia_yy
# eventually replace these with curve-fit values
from vehicle import C_D_0, C_L_0, C_L_alpha, C_L_delta_E, C_M_0, C_M_alpha, C_M_delta_E, K_CD

def degrees(alpha):
    """ Convert degrees to radians """
    return 180 / math.pi * alpha

def radians(alpha):
    """ Convert radians to degrees """
    return alpha * math.pi / 180

def get_angle_of_attack(u_B, w_B):
    """
    Given body-relative x and z velocities, calculates the angle of attack
    Input:
    u_B: body-relative x velocity (m/s)
    w_B: body-relative z velocity (m/s)
    Output:
    alpha: Angle of attack (rad)
    """
    return math.atan2(w_B, u_B)

def get_velocity(u_B, w_B):
    """
    Given body-relative x and z velocities, calculates the velocity
    Input:
    u_B: body-relative x velocity
    w_B: body-relative z velocity
    Output:
    V: total velocity
    """
    return math.sqrt(u_B**2 + w_B**2)

def find_C_L(alpha, delta_E, C_L_0=C_L_0, C_L_alpha=C_L_alpha, C_L_delta_E=C_L_delta_E):
    """
    Finds the coefficient of lift, given the inputs:
    Input:
    delta_E: Elevator angle
    alpha: Angle of attack
    Default:
    C_L_0: coefficient of lift at zero angle of attack, zero elevator
    C_L_alpha: linear approximation to increase in lift with angle of attack
    C_L_delta_E: linear approximation to increase in lift with elevator angle
    Output:
    C_L: total coefficient of lift
    """
    return C_L_0 + C_L_alpha*alpha + C_L_delta_E*delta_E

def find_C_D(C_L, C_D_0 = C_D_0, K = K_CD):
    """
    Finds the coefficient of drag.
    Input:
    C_L: Coefficient of lift
    Default:
    C_D_0: Zero-lift coefficient of drag
    K: Quadratic factor relating lift and drag
    """
    return C_D_0 + K*C_L**2

def find_C_M(alpha, delta_E, C_M_0=C_M_0, C_M_alpha=C_M_alpha, C_M_delta_E=C_M_delta_E):
    """
    Finds the moment coefficient.
    Input:
    alpha: Angle of attack (rad)
    delta_E: Elevator angle (rad)
    Default:
    C_M_0: Zero angle-of-attack moment coefficient
    C_M_alpha: Linear approximation to increase in moment with aoa
    C_M_delta_E: Linear approximation to increase in moment with delta_E
    Output:
    C_M: Total moment coefficient
    """
    return C_M_0 + C_M_alpha * alpha + C_M_delta_E * delta_E


def find_lift(V, C_L, Sref=Sref, rho=air_density):
    """
    Finds the lift given the velocity and coefficient of lift
    """
    return 1/2 * rho * V**2 * Sref * C_L

def find_drag(V, C_D, Sref=Sref, rho=air_density):
    """
    Finds the drag given the velocity and coefficient of drag
    """
    return 1/2 * rho * V**2 * Sref * C_D

def find_moment(V, C_M, Sref=Sref, rho=air_density, chord=cbar):
    """
    Finds the moment given the velocity and moment coefficient
    """
    return 1/2 * rho * V**2 * Sref * chord * C_M

def find_weight(m=acMass, g=gravity):
    """
    Finds the weight given the mass and gravity
    """
    return m*g

def dU_b_dt(L,D,alpha,T,q,w_B, m=acMass):
    """
    Given flight parameters, returns the body-relative x acceleration.
    """
    W = find_weight()
    # Force components
    lift = (L * math.sin(alpha))/m
    drag = -(D * math.cos(alpha))/m
    weight = -(W * sin(theta))/m
    thrust = T/m # thrust is aligned with the body x-axis
    # Accelerations
    euler_acceleration = -q * w_B
    return lift + drag + weight + thrust + euler_acceleration

def dW_b_dt(L,D,alpha,q,u_B, m=acMass):
    """
    Given flight parameters, returns the body-relative z acceleration.
    """
    W = find_weight()
    # Force components
    lift = (L * math.cos(alpha))/m
    drag = -(D * math.sin(alpha))/m
    weight = W * cos(theta)/m
    # Accelerations
    euler_acceleration = q * u_B
    return lift + drag + weight + euler_acceleration

def dq_dt(M, I_yy=inertia_yy):
    """
    Given flight parameters, returns the angular acceleration.
    """
    return M/I_yy

def dU_dt(U, X, _t):
    """
    Input:
    U: state array   
    U = [x_B, u_B, z_B, w_B, theta, q]
    X: command array 
    X = [delta_E, thrust]
    t: time
    Output:
    dU_dt: change in state array 
    dU_dt = [xdot_B, udot_B, zdot_B, wdot_B, thetadot_B, qdot_B]

    State vector U is chosen as:
    U[0] = x_B (body-relative forward location)
    U[1] = u_B (body-relative forward velocity)
    U[2] = z_B (body-relative downward location)
    U[3] = w_B (body-relative downward velocity)
    U[4] = theta (angle to the ground)
    U[5] = q (angular velocity, d(theta)/dt)
    """
    [x_B, u_B, z_B, w_B, theta, q] = U
    [delta_E, thrust] = X
    # Identity relations
    xdot_B = u_B
    zdot_B = w_B
    thetadot_B = q
    # Calculate angle of attack and velocity
    alpha = angle_of_attack(u_B, w_B)
    V = velocity(u_B, w_B)
    # Find flight coefficients
    C_L = find_C_L(alpha, delta_E)
    C_D = find_C_D(C_L)
    C_M = find_C_M(alpha, delta_E)
    # Find forces
    lift = find_lift(V, C_L)
    drag = find_drag(V, C_D)
    moment = find_moment(V, C_M)
    # Find accelerations
    udot_B = dU_b_dt(lift, drag, alpha, thrust, q, w_B)
    wdot_B = dW_b_dt(lift, drag, alpha, q, u_B)
    qdot = dq_dt(M)
    # dU_dt
    return [xdot_B, udot_B, zdot_B, wdot_B, thetadot_B, qdot_B]
