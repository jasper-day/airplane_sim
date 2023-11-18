"Plotting functionality for various questions"

# Plot results of integrated systems

from pprint import pprint
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from dynamics import find_state_parameters, find_initial_conditions, find_trim_conditions
from command import integrate_system, extract_param
import numpy as np
from gui_root_finder_iterables import find_system
from multiprocessing import Pool
from functools import partial, cache


class GraphWidget(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.view = FigureCanvas(Figure(figsize=(3,5)))
        self.ax = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        self.setLayout(vlayout)

def plot_parameter(graphWidget, param, U_integrated, time, **kwargs):
    "Take an integrated list of states and plot a particular parameter (see dynamics.py/find_state_parameters)"
    param_list = [find_state_parameters(U)[param] for U in U_integrated]
    graphWidget.ax.plot(time, param_list, **kwargs)
    graphWidget.ax.set_ylabel(param)
    graphWidget.ax.set_xlabel("Time (s)")

def plot_b2_answer(graphWidget, velocity=118, climb_angle=np.radians(2), starting_alt=1000, final_alt=2000, show_intermediate=True):
    assert(np.sign(climb_angle) == np.sign(final_alt - starting_alt))
    # Thomas is the oldest member, born 18 July, so default velocity is 118
    # get a decent starting guess by trigonometry
    climb_height = final_alt - starting_alt
    climb_dist = climb_height / np.sin(climb_angle)
    # estimated t_climb
    time_est = climb_dist / velocity
    print(f"estimated time: {time_est}")
    def f(t_climb):
        # returns final altitude given a t_climb
        # if the estimates weren't so good you might need to do some root finding on this :)
        total_time = t_climb + 300 # give some time for the oscillations to settle
        initial_condition = find_initial_conditions(velocity, 0, starting_alt, 0, total_time)
        trim_conditions = [
            find_trim_conditions(velocity, climb_angle, t_start=100),
            find_trim_conditions(velocity, gamma=0, t_start=100 + t_climb)
        ]
        res = integrate_system(initial_condition, trim_conditions)
        plot_parameter(graphWidget, "Altitude", res["U"], res["t"], color="black")
        # return average of last 50 altitude readings
        return np.average([find_state_parameters(U)["Altitude"] for U in res["U"][-50:]])
    
    graphWidget.ax.set_ylabel("Altitude")
    graphWidget.ax.axvline(100, color="red",linestyle='--')
    graphWidget.ax.axvline(100 + time_est, color="red", linestyle='--')
    final_alt_calculated = f(time_est)
    return {"t_climb": time_est, "final_alt": final_alt_calculated}

def find_system_plot(vel, gamma, method, err_type, e):
    res = find_system(vel, gamma, method, err_type, e)
    res["Angle of Attack (deg)"] = np.degrees(res["alpha"])
    res["Thrust (kN)"] = res["Thrust"] * 1e-3
    res["Flight Path Angle (deg)"] = np.degrees(res["gamma"])
    res["Velocity (m/s)"] = res["V"]
    res["Pitch Angle (deg)"] = np.degrees(res["pitch"])
    res["Elevator Inclination (deg)"] = np.degrees(res["delta_el"])
    return res


system_keys = [
    "Angle of Attack (deg)",
    "Thrust (N)",
    "Flight Path Angle (deg)",
    "Velocity (m/s)",
    "Pitch Angle (deg)",
    "Elevator Inclination (deg)"
]

def param_fix_gamma(graphWidget, param, gamma, vel_min, vel_max, method, err_type, e):
    vel_vals = np.linspace(vel_min, vel_max, 64)
    rs = map(partial(find_system_plot, gamma=gamma, method=method, err_type=err_type, e=e), vel_vals)
    params = [r[param] for r in rs]
    graphWidget.ax.plot(vel_vals, params)
    graphWidget.ax.set_xlabel('Velocity (m/s)')
    graphWidget.ax.set_ylabel(param)


def param_fix_vel(graphWidget, param,  vel, gamma_min, gamma_max, method, err_type, e):
    gamma_vals = np.linspace(gamma_min, gamma_max, 64)
    rs = map(partial(find_system_plot, vel=vel, method=method, err_type=err_type, e=e), gamma_vals)
    params = [r[param] for r in rs]
    errors = [r["alpha_error"] for r in rs]
    graphWidget.ax.plot(np.degrees(gamma_vals), params)
    graphWidget.ax.set_xlabel("Flight Path Angle (deg)")
    graphWidget.ax.set_ylabel(param)



def make_sample_plot(fig, axs, U):
    "Plot system results on a 4x2 subplot"
    axs[0,0].plot(U["t"], extract_param(U, "u_B"))
    axs[0,0].set_ylabel("$u_B$")
    axs[0,1].plot(U["t"], extract_param(U, "w_B"))
    axs[0,1].set_ylabel("$w_B$")
    axs[1,0].plot(U["t"], extract_param(U, "q"))
    axs[1,0].set_ylabel("q")
    axs[1,1].plot(U["t"], extract_param(U, "theta (deg)"))
    axs[1,1].set_ylabel(r'$\theta$')
    axs[2,0].plot(U["t"], extract_param(U, "gamma (deg)"))
    axs[2,0].set_ylabel(r"$\gamma$")
    axs[2,1].plot(U["t"], extract_param(U, "z_E"))
    axs[2,1].set_ylabel(r"$z_E$")
    axs[3,0].plot(U["t"], extract_param(U, "alpha (deg)"))
    axs[3,0].set_ylabel(r"$\alpha$")
    axs[3,1].plot(U["t"], extract_param(U, "altitude"))
    axs[3,1].set_ylabel("altitude")
    fig.tight_layout()
    return fig