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

if __name__ == "__main__":
    gw = TestGraph()
    plot_b2_answer(gw)
    plt.show()