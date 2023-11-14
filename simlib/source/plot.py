"Plotting functionality for various questions"

# Plot results of integrated systems

import source.root_finder
from pprint import pprint
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget
from dynamics import find_system_parameters

class GraphWidget(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=None):
        super(TestGraph, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)        

def plot_parameter(param, graphWidget, U_integrated, t):
    param_list = [find_system_parameters(U)[param] for U in U_integrated]
    graphWidget.ax.clear()
    graphWidget.ax.plot(time, param_list)
    graphWidget.ax.set_ylabel(param)
    graphWidget.ax.set_xlabel("time (s)")





pprint(source.root_finder.find_system(100, 0))

def plot_curve_fit_output(fig, ax):
    # fig, axs must be a 2x4 subplot
    pass