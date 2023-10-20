# 3-DOF simulation for airplane
# State vector U is chosen as:
# U[0] = x_B (body-relative forward location)
# U[1] = u_B (body-relative forward velocity)
# U[2] = z_B (body-relative downward location)
# U[3] = w_B (body-relative downward velocity)
# U[4] = theta (angle to the ground)
# U[5] = q (angular velocity, d(theta)/dt)

import math

from env import gravity, air_density
from vehicle import Sref, cbar, acMass, inertia_yy
from vehicle import C_D_0, C_L_0, C_L_alpha, C_L_delta_E, C_M_0, C_M_alpha, C_M_delta_E, K_CD

def get_angle_of_attack(u_B, w_B):
    """
    Given body-relative x and z velocities, calculates the angle of attack
    Input:
    u_B: body-relative x velocity
    w_B: body-relative z velocity
    Output:
    alpha: Angle of attack
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
    alpha: Angle of attack
    delta_E: Elevator angle
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

def dU_b_dt(L,D,alpha,T,q,w_B,m=acMass, g=gravity):
    """
    Given flight parameters, returns the body-relative x acceleration.
    """
    W = find_weight(m, g)
    # Forces 
    lift = (L * math.sin(alpha))/m
    drag = -(D * math.cos(alpha))/m
    weight = -(W * sin(theta))/m
    thrust = T/m # thrust is aligned with the body x-axis
    # Accelerations
    euler_acceleration = -q * w_B
    return lift + drag + weight + thrust + euler_acceleration

def dU_dt(U, X, _t):
    """
    Input:
    U: state array   [x_B, u_B, z_B, w_B, theta, q]
    X: command array [delta_E, thrust]
    t: time
    Output:
    dU_dt: change in state array [xdot_B, udot_B, zdot_B, wdot_B, thetadot_B, qdot_B]
    """
    [x_B, u_B, z_B, w_B, theta, q] = U
    [delta_E, thrust] = X
    # Identity relations
    xdot_B = u_B
    zdot_B = w_B
    thetadot_B = q
    # Calculate angle of attack
    alpha = angle_of_attack(u_B, w_B)
    gamma = theta - alpha
    # remaining: find udot, wdot, qdot
    

    # dU_dt
    return [xdot_B, udot_B, zdot_B, wdot_B, thetadot_B, qdot_B]
