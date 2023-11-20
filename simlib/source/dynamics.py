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
from curve_fit import C_D_0, C_L_0, C_L_alpha, C_L_delta_el, C_M_0, C_M_alpha, C_M_delta_el, K_C_D
import inspect

def rad2deg(alpha):
    """ Convert radians to degrees """
    return 180 / math.pi * alpha

def deg2rad(alpha):
    """ Convert degrees to radians """
    return alpha * math.pi / 180

def find_angle_of_attack(u, w):
    """Given body-relative x and z velocities, calculates the angle of attack
    Input:
    u_B: body-relative x velocity (m/s)
    w_B: body-relative z velocity (m/s)
    Output:
    alpha: Angle of attack (rad)"""
    # if u == 0:
    #     return math.pi/2 * np.sign(w)
    # else:
    return math.atan2(w, u)

def get_speed(u, w):
    """Given x and z velocities, calculates the speed"""
    return math.sqrt(u**2 + w**2)

def get_body_velocities(speed, angle_of_att):
    u_B = speed * math.cos(angle_of_att)
    w_B = speed * math.sin(angle_of_att)
    return np.array([u_B, w_B])

def earth2body(x_E: float, z_E: float, theta):
    "Rotates a point in global x and z coordinates to a body-relative frame"
    rot_arr = np.array([[np.cos(theta), -np.sin(theta)],
                        [np.sin(theta), np.cos(theta)]])
    return rot_arr @ np.array([x_E, z_E])

def body2earth(x_B: float, z_B: float, theta):
    "Rotates a point in body-relative x and z coordinates to a global frame"
    rot_arr = np.array([[np.cos(theta), np.sin(theta)],
                        [-np.sin(theta), np.cos(theta)]])
    return rot_arr @ np.array([x_B, z_B])

def find_C_L(alpha, delta_el, C_L_0=C_L_0, C_L_alpha=C_L_alpha, 
C_L_delta_el=C_L_delta_el):
    """Finds the coefficient of lift, given angle of attack and elevators
    Input:
    delta_el: Elevator angle (rad)
    alpha: Angle of attack (rad)
    """
    return C_L_0 + C_L_alpha*alpha + C_L_delta_el*delta_el

def find_C_D(C_L, C_D_0=C_D_0, K=K_C_D):
    """Finds the coefficient of drag, given the lift coefficient
    Input:
    C_L: Coefficient of lift
    """
    return C_D_0 + K*C_L**2

def find_C_M(alpha, delta_el, C_M_0=C_M_0, C_M_alpha=C_M_alpha, C_M_delta_el=C_M_delta_el):
    """Finds the moment coefficient.
    Input:
    alpha: Angle of attack (rad)
    delta_el: Elevator angle (rad)"""
    return C_M_0 + C_M_alpha * alpha + C_M_delta_el * delta_el


def find_lift(speed, C_L, Sref=Sref, rho=air_density):
    """Finds the lift given the velocity and coefficient of lift"""
    return 1/2 * rho * speed**2 * Sref * C_L

def find_drag(speed, C_D, Sref=Sref, rho=air_density):
    """Finds the drag given the velocity and coefficient of drag"""
    return 1/2 * rho * speed**2 * Sref * C_D

def find_moment(speed, C_M, Sref=Sref, rho=air_density, chord=cbar):
    """Finds the moment given the velocity and moment coefficient"""
    return 1/2 * rho * speed**2 * Sref * chord * C_M

def find_weight(m=acMass, g=gravity):
    """Finds the weight given the mass and gravity"""
    return m*g

def du_B_dt(L,D,alpha,T,q,w_B, theta, m=acMass):
    """Given flight parameters, returns the body-relative x acceleration."""
    # See pdf, page 4
    W = find_weight()
    # Force components
    lift = (L * math.sin(alpha))/m
    drag = -(D * math.cos(alpha))/m
    weight = -(W * math.sin(theta))/m
    thrust = T/m # thrust is aligned with the body x-axis
    # Accelerations
    euler_acceleration = -q * w_B
    return lift + drag + weight + thrust + euler_acceleration

def dw_B_dt(L,D,alpha,q,u_B, theta, m=acMass):
    """Given flight parameters, returns the body-relative z acceleration."""
    W = find_weight()
    # Force components
    lift = -(L * math.cos(alpha))/m
    drag = -(D * math.sin(alpha))/m
    weight = W * math.cos(theta)/m
    # Accelerations
    euler_acceleration = q * u_B
    return lift + drag + weight + euler_acceleration

def dq_dt(M, I_yy=inertia_yy):
    """Given flight parameters, returns the angular acceleration."""
    return M/I_yy

def dU_dt(t, U, X):
    """Find rate of change of the state array.
    Input:
    U: state array   
    U = [x_E, z_E, u_B, w_B, theta, q]
    X: function returning command array
    X(t) = [delta_el, thrust]
    t: time
    Output:
    dU_dt: rate of change of state array"""
    [x_earth, z_earth, u_body, w_body, theta, q] = U
    [delta_el, thrust] = X(t)
    # Calculate angle of attack and velocity
    alpha = find_angle_of_attack(u_body, w_body)
    speed = get_speed(u_body, w_body)
    # Find flight coefficients
    C_L = find_C_L(alpha, delta_el)
    C_D = find_C_D(C_L)
    C_M = find_C_M(alpha, delta_el)
    # Find forces
    lift = find_lift(speed, C_L)
    drag = find_drag(speed, C_D)
    moment = find_moment(speed, C_M)
    # Find accelerations
    udot = du_B_dt(lift, drag, alpha, thrust, q, w_body, theta)
    wdot = dw_B_dt(lift, drag, alpha, q, u_body, theta)
    qdot = dq_dt(moment)
    [xdot, zdot] = body2earth(u_body, w_body, theta)
    # dU_dt
    return np.array([xdot, zdot, udot, wdot, q, qdot])

def find_U_0(system, altitude=None):
    """ Find the state array U given an altitude and the system"""
    if altitude == None:
        altitude = system["altitude"]
    body_velocities = get_body_velocities(system["V"], system["alpha"])
    theta = system["alpha"] + system["gamma"]
    z_E = -altitude # earth-relative z-position
    x_E = 0 # earth-relative x-position
    try:
        q = system["q"]
    except KeyError:
        q = 0
    return np.array([
        x_E, z_E,
        body_velocities[0], body_velocities[1],
        theta, q
    ])
    

def find_initial_conditions(velocity, gamma, altitude, q, total_time):
    if velocity == 0:
        raise ValueError("Must have nonzero starting velocity")
    if total_time == 0:
        raise ValueError("Must have nonzero simulation time")
    initial_conditions = find_system(velocity, gamma)
    initial_conditions["altitude"] = altitude
    initial_conditions["q"] = q
    initial_conditions["U_0"] = find_U_0(initial_conditions)
    initial_conditions["t_total"] = total_time
    return initial_conditions

def find_trim_conditions(velocity, gamma, t_start):
    from root_finder import find_system
    trim_conditions = find_system(velocity, gamma)
    trim_conditions["t_start"] = t_start
    return trim_conditions

def find_state_parameters(U):
    "Given a state U, extracts all useful information about the state."
    [x_E, z_E, u_B, w_B, theta, q] = U
    alpha = find_angle_of_attack(u_B, w_B)
    # Position isn't a vector, but velocity is
    [u_E, w_E] = body2earth(u_B, w_B, theta)
    return {
        "Body X Velocity": u_B,
        "Body Z Velocity": w_B,
        "Speed (m/s)": get_speed(u_B, w_B),
        "Pitch Angle (rad)": theta,
        "Pitch Angle (deg)": rad2deg(theta),
        "Angle of Attack (rad)": alpha,
        "Angle of Attack (deg)": rad2deg(alpha),
        "Flight Path Angle (rad)": theta - alpha,
        "Flight Path Angle (deg)": rad2deg(theta - alpha),
        "Angular Velocity (rad/s)": q,
        "Angular Velocity (deg/s)": rad2deg(q),
        "Global x Pos": x_E,
        "Global x Vel": u_E,
        "Global z Pos": z_E,
        "Global z Vel": w_E,
        "Altitude": -z_E,
    }

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from root_finder import find_system
    from scipy.integrate import solve_ivp
    from pprint import pprint
    X1 = [-0.0520, 2755.17]
    X2 = [-0.0572, 2755.17]
    X = lambda t: X1 if t < 100 else X2
    U_0 = find_U_0(find_system(100, 0), 2000)
    print("initial conditions")
    pprint(find_state_parameters(U_0))
    res = solve_ivp(dU_dt,(0,300), U_0, max_step=1, args=(X,))
    pprint(res)
    t = res['t']
    Us = res['y'].T
    params = [find_state_parameters(U) for U in Us]
    find_param = lambda name: [param[name] for param in params]
    fig,axs = plt.subplots(4,2)
    axs[0,0].plot(t, Us[:,2])
    axs[0,0].set_ylabel("uB (ms\u207B\u00B9) ")
    axs[0,0].set_xlabel("time (s)")
    axs[0,1].plot(t, Us[:,3])
    axs[0,1].set_ylabel("wB (ms\u207B\u00B9)")
    axs[0,1].set_xlabel("time (s)")
    axs[1,0].plot(t, Us[:, 5])
    axs[1,0].set_ylabel("q (rads\u207B\u00B9)")
    axs[1,0].set_xlabel("time (s)")
    axs[1,1].plot(t, rad2deg(Us[:, 4]))
    axs[1,1].set_ylabel("theta (rad)")
    axs[1,1].set_xlabel("time (s)")
    axs[2,0].plot(t, find_param("Flight Path Angle (deg)"))
    axs[2,0].set_ylabel("$\\gamma$ (rad)")
    axs[2,0].set_xlabel("time (s)")
    axs[2,1].plot(t, find_param("Global z Pos"))
    axs[2,1].set_ylabel("z_E")
    axs[2,1].set_xlabel("time (s)")
    axs[3,0].plot(t, find_param("Angle of Attack (deg)"))
    axs[3,0].set_ylabel("$\\alpha$ (rad)")
    axs[3,0].set_xlabel("time (s)")
    axs[3,1].plot(t, -Us[:,1])
    axs[3,1].set_ylabel("altitude (m)")
    axs[3,1].set_xlabel("time (s)")
    fig.tight_layout()
    plt.show()