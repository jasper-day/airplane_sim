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

def test_velocity_conversion():
    us = ws = np.arange(-100,100,10)
    testlist = [np.array([u, w]) for u in us for w in ws]
    speeds = [get_speed(u, w) for u in us for w in ws]
    alphas = [find_angle_of_attack(u, w) for u in us for w in ws]
    testoutput = [get_body_velocities(speeds[i], alphas[i]) for i in range(len(alphas))]
    assert np.all([np.isclose(testlist[i], testoutput[i]) for i in range(len(testlist))])
    

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
    Default:
    C_L_0: coefficient of lift at zero angle of attack, zero elevator
    C_L_alpha: linear approximation to increase in lift with angle of attack
    C_L_delta_el: linear approximation to increase in lift with elevator angle
    Output:
    C_L: total coefficient of lift"""
    return C_L_0 + C_L_alpha*alpha + C_L_delta_el*delta_el

def find_C_D(C_L, C_D_0=C_D_0, K=K_C_D):
    """Finds the coefficient of drag, given the lift coefficient
    Input:
    C_L: Coefficient of lift
    Default:
    C_D_0: Zero-lift coefficient of drag
    K: Quadratic factor relating lift and drag"""
    return C_D_0 + K*C_L**2

def find_C_M(alpha, delta_el, C_M_0=C_M_0, C_M_alpha=C_M_alpha, C_M_delta_el=C_M_delta_el):
    """Finds the moment coefficient.
    Input:
    alpha: Angle of attack (rad)
    delta_el: Elevator angle (rad)
    Default:
    C_M_0: Zero angle-of-attack moment coefficient
    C_M_alpha: Linear approximation to increase in moment with aoa
    C_M_delta_el: Linear approximation to increase in moment with delta_el
    Output:
    C_M: Total moment coefficient"""
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
    U[5] = q (angular velocity, d(theta)/dt)"""
    [x_B, u_B, z_B, w_B, theta, q] = U
    if inspect.isfunction(X):
        [delta_el, thrust] = X(t)
    else:
        [delta_el, thrust] = X
    # Calculate angle of attack and velocity
    alpha = find_angle_of_attack(u_B, w_B)
    speed = get_speed(u_B, w_B)
    # Find flight coefficients
    C_L = find_C_L(alpha, delta_el)
    C_D = find_C_D(C_L)
    C_M = find_C_M(alpha, delta_el)
    # Find forces
    lift = find_lift(speed, C_L)
    drag = find_drag(speed, C_D)
    moment = find_moment(speed, C_M)
    # Find accelerations
    udot_B = du_B_dt(lift, drag, alpha, thrust, q, w_B, theta)
    wdot_B = dw_B_dt(lift, drag, alpha, q, u_B, theta)
    qdot = dq_dt(moment)
    # dU_dt
    return np.array([u_B, udot_B, w_B, wdot_B, q, qdot])

def find_U_0(system, altitude):
    """ Find the state array U given an altitude and the system"""
    body_velocities = get_body_velocities(system["V"], system["alpha"])
    theta = system["alpha"] + system["gamma"]
    z_E = -altitude # earth-relative z-position
    x_E = 0 # earth-relative x-position
    body_frame = earth2body(x_E, z_E, theta)
    q = 0
    return np.array([
        body_frame[0],
        body_velocities[0],
        body_frame[1],
        body_velocities[1],
        theta,
        q
    ])

def find_system_parameters(U):
    "Given a state U, extracts all useful information about the state."
    [x_B, u_B, z_B, w_B, theta, q] = U
    [x_E, z_E] = body2earth(x_B, z_B, theta)
    alpha = find_angle_of_attack(u_B, w_B)
    [u_E, w_E] = body2earth(u_B, w_B, theta)
    return {
        "x_B": x_B,
        "u_B": u_B,
        "z_B": z_B,
        "w_B": w_B,
        "speed": get_speed(u_B, w_B),
        "theta": theta,
        "theta (deg)": rad2deg(theta),
        "alpha": alpha,
        "alpha (deg)": rad2deg(alpha),
        "gamma": theta - alpha,
        "gamma (deg)": rad2deg(theta - alpha),
        "q": q,
        "q (deg/s)": rad2deg(q),
        "x_E": x_E,
        "u_E": u_E,
        "z_E": z_E,
        "w_E": w_E,
        "altitude": -z_E,
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
    pprint(find_system_parameters(U_0))
    res = solve_ivp(dU_dt,(0,300), U_0, max_step=0.01, args=(X,))
    pprint(res)
    t = res['t']
    Us = res['y'].T
    params = [find_system_parameters(U) for U in Us]
    find_param = lambda name: [param[name] for param in params]
    fig,axs = plt.subplots(4,2)
    axs[0,0].plot(t, Us[:,1])
    axs[0,0].set_ylabel("uB")
    axs[0,1].plot(t, Us[:,3])
    axs[0,1].set_ylabel("wB")
    axs[1,0].plot(t[:-2], (np.diff(Us[:,0]) / np.diff(t))[:-1])
    axs[1,0].set_ylabel("uB (diff)")
    axs[1,1].plot(t[:-2], (np.diff(Us[:,2]) / np.diff(t))[:-1])
    axs[1,1].set_ylabel("wb (diff)")
    axs[2,0].plot(t, find_param("x_B"))
    axs[2,0].set_ylabel("xB")
    axs[2,1].plot(t, find_param("z_E"))
    axs[2,1].set_ylabel("z_E")
    axs[3,0].plot(t, find_param("z_B"))
    axs[3,0].set_ylabel("zB")
    axs[3,1].plot(t, - Us[:,0] * np.sin(Us[:,5]) + Us[:,2] * np.cos(Us[:, 5]))
    axs[3,1].set_ylabel("altitude")
    fig.tight_layout()
    plt.show()
