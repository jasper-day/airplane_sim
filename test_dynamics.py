from aero_table import CD, CL, CM, CM_el, CL_el, alpha, delta_el
import numpy as np
from vehicle import Sref, cbar, acMass, inertia_yy
from env import air_density, gravity
import math
from numpy.polynomial.polynomial import polyfit

CL_coeffs = polyfit(np.radians(alpha), CL, 1)
CM_coeffs = polyfit(np.radians(alpha), CM, 1)
CL_el_coeffs = polyfit(np.radians(delta_el), CL_el, 1)
CM_el_coeffs = polyfit(np.radians(delta_el), CM_el, 1)
CD_coeffs = polyfit(CL, CD, 2)
C_L_0 = CL_coeffs[0]
C_L_alpha = CL_coeffs[1]
C_M_0 = CM_coeffs[0]
C_M_alpha = CM_coeffs[1]
C_L_delta_el = CL_el_coeffs[1]
C_M_delta_el = CM_el_coeffs[1]
C_D_0 = CD_coeffs[0]
K_C_D = CD_coeffs[2]

def dU_dt(t, U, X):
    [delta_el, thrust] = X(t)
    [x, u, z, w, theta, q] = U
    alpha = math.atan2(w, u)
    CL = C_L_0 + C_L_alpha * alpha + C_L_delta_el * delta_el
    CD = C_D_0 + K_C_D * CL**2
    CM = C_M_0 + C_M_alpha * alpha + C_M_delta_el * delta_el
    speed = np.sqrt(u**2 + w**2)
    rho = air_density
    L = 0.5 * rho * speed**2 * Sref * CL
    D = 0.5 * rho * speed**2 * Sref * CD
    M = 0.5 * rho * speed**2 * Sref * cbar * CM
    W = acMass * gravity
    m = acMass
    du_dt = L/m * np.sin(alpha) - D/m * np.cos(alpha) - q*w - W/m * np.sin(theta) + thrust/m
    dw_dt = -L/m * np.cos(alpha) - D/m * np.sin(alpha) + q*u + W/m * np.cos(theta)
    dq_dt = M/inertia_yy
    return np.array([u, du_dt, w, dw_dt, q, dq_dt])


# find initial conditions
initial_conditions = {"alpha": 0.0164, "theta": 0.01646, "Thrust": 2755.17, "delta_el": -0.0520, "V": 100}

theta = initial_conditions["theta"]

altitude = 2000

z_earth = -altitude
x_earth = 0
# ccw rotation through theta
body_coords = np.array([[np.cos(theta), -np.sin(theta)], 
                   [np.sin(theta), np.cos(theta)]]) @ np.array([x_earth, z_earth])
print(body_coords)

u_body = initial_conditions["V"] * np.cos(initial_conditions["alpha"])
w_body = initial_conditions["V"] * np.sin(initial_conditions["alpha"])

print(f"ub: {u_body}")
print(f"vb: {w_body}")

q = 0

U_0 = np.array([body_coords[0], u_body, body_coords[1], w_body, theta, q])

X_0 = np.array([initial_conditions["delta_el"], initial_conditions["Thrust"]])
X_1 = np.array([initial_conditions["delta_el"] * 1.1, initial_conditions["Thrust"]])
X_0p = np.array([-0.0520, 2755.17])
X_1p = np.array([-0.0572, 2755.17])

X = lambda t: X_0p if t < 100 else X_1p

# t = np.linspace(0, 300, 1000)

# U = rk4_integrate(dU_dt, U_0, X, t)
import scipy.integrate as integrate
res = integrate.solve_ivp(dU_dt,(0,300), U_0, max_step=0.01, args=(X,))
U = res["y"].T
t = res["t"]

x_B = U[:, 0]
z_B = U[:, 2]
theta = U[:, 4]

x_E = [np.cos(theta[i]) * x_B[i] + np.sin(theta[i]) * z_B[i] for i in range(len(theta))]
z_E = [np.cos(theta[i]) * z_B[i] + -np.sin(theta[i]) * x_B[i] for i in range(len(theta))]

import matplotlib.pyplot as plt

fig, axs = plt.subplots(3,2)

# axs[0,0].plot(t, x_E, label='xpos', color='C0')
axs[0,0].plot(t[:-2], (np.diff(U[:,0])/ np.diff(t))[:-1], label='uB (finite diff)', color='C0')
axs[0,1].plot(t, U[:, 1], label='uB', color='C1')
axs[1,0].plot(t, z_E, label='zpos', color='C2')
axs[1,1].plot(t, U[:, 3], label='wB', color='C3')
axs[2,0].plot(t, np.degrees(U[:, 4]), label='theta (deg)', color='C4')
axs[2,1].plot(t, U[:, 5], label='q', color='C5')
fig.legend()
plt.show()