import sys
sys.path.append('simlib/source/')
from gui.simulator_mwc import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QLineEdit,
    QLabel,
)

from GUI import TestGraph
from source.plot import GraphWidget, plot_parameter
from root_finder import find_system
from source.command import integrate_system


class SimWindow(QMainWindow, Ui_MainWindow):                           
    def __init__(self, parent = None):
        super(SimWindow, self).__init__(parent)
        self.setupUi(self)
        self.graph = GraphWidget()
        self.graph_layout = QHBoxLayout()
        self.graph_layout.addWidget(self.graph)
        self.graph_output.setLayout(self.graph_layout)
        self.trim_list = [] # data for commands
        self.initial_conditions = {} # data for initial conditions
    def add_trim():
        if self.trim_vel == 0:
            return
        system = find_system(self.trim_vel, self.trim_gamma)
        system['t_start'] = self.trim_time_start
        self.trim_list.append(system)
    def clear_trims():
        self.trim_list = []
    def remove_last_trim():
        self.trim_list.pop()
    def update_initial_conditions():
        if self.init_vel == 0:
            return
        if self.simulation_time == 0:
            return
        self.initial_conditions = find_system(self.init_vel, self.init_gamma)
        self.initial_conditions["altitude"] = self.init_altitude
        self.initial_conditions["q"] = self.init_angvel
        self.initial_conditions["t_total"] = self.init_total_time
    def run_simulation():
        self.sim_result = integrate_system(self.initial_conditions, self.trim_list)
    def mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimuPlane™ 0.1.0")
        layout = QGridLayout(self)
        
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("simlib/p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")
        
        self.button1 = QPushButton("Start", self)
        self.button1.clicked.connect(self.simwin)
        self.button2 = QPushButton("Quit",self)
        self.button2.clicked.connect(sys.exit)
        
        layout.addWidget(self.label, 0,0)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,2,0)
        self.setLayout(layout)

    def simwin(self):
        self.simwin = SimWindow()
        self.simwin.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())