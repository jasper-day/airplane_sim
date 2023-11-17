"""
Code for flight mechanics

Contains functions for calculating aerodynamic forces and moments, as well as
the equations of motion for the airplane.

All units should be normalized to SI units
All angles in radians
"""

import math
import numpy as np
from env import gravity, air_density
from vehicle import Sref, cbar, acMass, inertia_yy
# eventually replace these with curve-fit values
from curve_fit import C_D_0, C_L_0, C_L_alpha, C_L_delta_el, C_M_0, C_M_alpha, C_M_delta_el, K_C_D

def rad2deg(alpha):
    """ Convert radians to degrees """
    return 180 / math.pi * alpha

def deg2rad(alpha):
    """ Convert degrees to radians """
    return alpha * math.pi / 180

def find_angle_of_attack(u_B, w_B):
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

def get_body_velocities(V, alpha):
    u_B = V * math.cos(alpha)
    w_B = V * math.sin(alpha)
    return {"u_B": u_B, "w_B": w_B}

def earth2body(x_E, z_E, theta):
    "Rotates global x and z coordinates to a body-relative frame"
    x_B = x_E * math.cos(theta) - z_E * math.sin(theta)
    z_B = x_E * math.sin(theta) + z_E * math.cos(theta)
    return {"x": x_B, "z": z_B}

def body2earth(x_B, z_B, theta):
    "Rotates body-relative x and z coordinates to a global frame"
    x_E =  x_B * math.cos(theta) + z_B * math.sin(theta)
    z_E = -x_B * math.sin(theta) + z_B * math.cos(theta)
    return {"x": x_E, "z": z_E}

def find_C_L(alpha, delta_el, C_L_0=C_L_0, C_L_alpha=C_L_alpha, 
C_L_delta_el=C_L_delta_el):
    """
    Finds the coefficient of lift, given the inputs:
    Input:
    delta_el: Elevator angle
    alpha: Angle of attack
    Default:
    C_L_0: coefficient of lift at zero angle of attack, zero elevator
    C_L_alpha: linear approximation to increase in lift with angle of attack
    C_L_delta_el: linear approximation to increase in lift with elevator angle
    Output:
    C_L: total coefficient of lift
    """
    return C_L_0 + C_L_alpha*alpha + C_L_delta_el*delta_el

def find_C_D(C_L, C_D_0 = C_D_0, K = K_C_D):
    """
    Finds the coefficient of drag.
    Input:
    C_L: Coefficient of lift
    Default:
    C_D_0: Zero-lift coefficient of drag
    K: Quadratic factor relating lift and drag
    """
    return C_D_0 + K*C_L**2

def find_C_M(alpha, delta_el, C_M_0=C_M_0, C_M_alpha=C_M_alpha, C_M_delta_el=C_M_delta_el):
    """
    Finds the moment coefficient.
    Input:
    alpha: Angle of attack (rad)
    delta_el: Elevator angle (rad)
    Default:
    C_M_0: Zero angle-of-attack moment coefficient
    C_M_alpha: Linear approximation to increase in moment with aoa
    C_M_delta_el: Linear approximation to increase in moment with delta_el
    Output:
    C_M: Total moment coefficient
    """
    return C_M_0 + C_M_alpha * alpha + C_M_delta_el * delta_el


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

def dU_b_dt(L,D,alpha,T,q,w_B, theta, m=acMass):
    """
    Given flight parameters, returns the body-relative x acceleration.
    """
    W = find_weight()
    # Force components
    lift = (L * math.sin(alpha))/m
    drag = -(D * math.cos(alpha))/m
    weight = -(W * math.sin(theta))/m
    thrust = T/m # thrust is aligned with the body x-axis
    # Accelerations
    euler_acceleration = -q * w_B
    return lift + drag + weight + thrust + euler_acceleration

def dW_b_dt(L,D,alpha,q,u_B, theta, m=acMass):
    """
    Given flight parameters, returns the body-relative z acceleration.
    """
    W = find_weight()
    # Force components
    lift = (L * math.cos(alpha))/m
    drag = -(D * math.sin(alpha))/m
    weight = W * math.cos(theta)/m
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
    X = [delta_el, thrust]
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
    [delta_el, thrust] = X
    # Identity relations
    xdot_B = u_B
    zdot_B = w_B
    thetadot = q
    # Calculate angle of attack and velocity
    alpha = find_angle_of_attack(u_B, w_B)
    V = get_velocity(u_B, w_B)
    # Find flight coefficients
    C_L = find_C_L(alpha, delta_el)
    C_D = find_C_D(C_L)
    C_M = find_C_M(alpha, delta_el)
    # Find forces
    lift = find_lift(V, C_L)
    drag = find_drag(V, C_D)
    moment = find_moment(V, C_M)
    # Find accelerations
    udot_B = dU_b_dt(lift, drag, alpha, thrust, q, w_B, theta)
    wdot_B = dW_b_dt(lift, drag, alpha, q, u_B, theta)
    qdot = dq_dt(moment)
    # dU_dt
    return np.array([xdot_B, udot_B, zdot_B, wdot_B, thetadot, qdot])

def find_U_0(system, altitude):
    """ Find the state array U given an altitude and the system """
    body_velocities = get_body_velocities(system["V"], system["alpha"])
    theta = system["alpha"] + system["gamma"]
    z_E = -altitude # earth-relative z-position
    x_E = 0 # earth-relative x-position
    body_frame = earth2body(x_E, z_E, theta)
    q = 0
    return np.array([
        body_frame["x"],
        body_velocities["u_B"],
        body_frame["z"],
        body_velocities["w_B"],
        theta,
        q
    ])

def find_system_parameters(U):
    [x_B, u_B, z_B, w_B, theta, q] = U
    earth_frame = body2earth(x_B, z_B, theta)
    alpha = find_angle_of_attack(u_B, w_B)
    earth_velocities = body2earth(u_B, w_B, theta)
    return {
        "x_B": x_B,
        "u_B": u_B,
        "z_B": z_B,
        "w_B": w_B,
        "theta": theta,
        "alpha": alpha,
        "alpha (deg)": rad2deg(alpha),
        "gamma": theta - alpha,
        "gamma (deg)": rad2deg(theta - alpha),
        "q": q,
        "x_E": earth_frame["x"],
        "u_E": earth_velocities["x"],
        "z_E": earth_frame["z"],
        "w_E": earth_velocities["z"],
        "altitude": -earth_frame["z"],
    }
