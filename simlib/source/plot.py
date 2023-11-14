"Plotting functionality for various questions"

# Plot results of integrated systems

from pprint import pprint
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget
from dynamics import find_system_parameters
from command import integrate_system
from root_finder import find_system
import numpy as np

class GraphWidget(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=QWidget):
        super(TestGraph, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

class TestGraph():
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()

def plot_parameter(graphWidget, param, U_integrated, time):
    param_list = [find_system_parameters(U)[param] for U in U_integrated]
    graphWidget.ax.plot(time, param_list)
    graphWidget.ax.set_ylabel(param)
    graphWidget.ax.set_xlabel("time (s)")

def plot_b2_answer(graphWidget):
    U = 18 # Thomas is the oldest member, born 18 July
    trim_conditions = [
        find_system(100 + U, 0), # steady level flight
        find_system(100 + U, np.deg2rad(2)), # climbing flight
        find_system(100 + U, 0), # steady level flight
    ]
    pprint(trim_conditions[1])
    climb_durations = np.arange(100,300,20)
    total_time = 1200
    for t_climb in climb_durations:
        time_starts = [0, 100, 100 + t_climb]
        res = integrate_system(trim_conditions, time_starts, total_time, 0.1, starting_altitude=1000)
        plot_parameter(graphWidget, "altitude", res["U"], res["t"])

def plot_curve_fit_output(fig, ax):
    # fig, axs must be a 2x4 subplot
    pass

def make_sample_plot(fig, axs):
    "Plot system results on a 4x2 subplot"
    axs[0,0].plot(U_i["t"], extract_param("u_B"))
    axs[0,0].set_ylabel("$u_B$")
    axs[0,1].plot(U_i["t"], extract_param("w_B"))
    axs[0,1].set_ylabel("$w_B$")
    axs[1,0].plot(U_i["t"], extract_param("q"))
    axs[1,0].set_ylabel("q")
    axs[1,1].plot(U_i["t"], extract_param("theta (deg)"))
    axs[1,1].set_ylabel(r'$\theta$')
    axs[2,0].plot(U_i["t"], extract_param("gamma (deg)"))
    axs[2,0].set_ylabel(r"$\gamma$")
    axs[2,1].plot(U_i["t"], extract_param("z_E"))
    axs[2,1].set_ylabel(r"$z_E$")
    axs[3,0].plot(U_i["t"], extract_param("alpha (deg)"))
    axs[3,0].set_ylabel(r"$\alpha$")
    axs[3,1].plot(U_i["t"], extract_param("altitude"))
    axs[3,1].set_ylabel("altitude")
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    gw = TestGraph()
    plot_b2_answer(gw)
    plt.show()