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

from source.plot import GraphWidget, plot_parameter, find_state_parameters
from source.root_finder import find_system
from source.command import integrate_system
from source.dynamics import find_U_0


class SimWindow(QMainWindow, Ui_MainWindow):
    # Ui_MainWindow is compiled from ui/simulator-mw.ui using pyside6-designer
    def __init__(self, parent = None):
        super(SimWindow, self).__init__(parent)
        # create the Ui_MainWindow object
        self.setupUi(self)
        # output plotting (from source.plot)
        self.graph = GraphWidget()
        # add the graph widget to the graph_output widget
        graph_layout = QHBoxLayout()
        graph_layout.addWidget(self.graph)
        self.graph_output.setLayout(self.graph_layout)
        # trim commands are a list(dict)
        self.trim_list = [] 
        # initial conditions are a dict
        self.initial_conditions = {}
        # callbacks
        self.add_trim_btn.clicked.connect(self.add_trim)
        self.del_prev_trim_btn.clicked.connect(self.remove_last_trim)
        self.clear_trims_btn.clicked.connect(self.clear_trims)
        self.run_simulation_btn.clicked.connect(self.run_simulation)
        self.update_plot_btn.clicked.connect(self.update_plot)
        self.exit_btn.clicked.connect(self.mainwindow)
        self.graph_selector.currentIndexChanged.connect(self.update_plot)
    def add_trim(self):
        # get trim commands
        if self.trim_vel.value() == 0:
            return
        system = find_system(self.trim_vel.value(), np.radians(self.trim_gamma.value()))
        system['t_start'] = self.trim_time_start.value()
        self.trim_list.append(system)
        self.trim_list.sort(key=lambda x: x["t_start"])
        self.updateTable()
    def clear_trims(self):
        self.trim_list = []
        self.updateTable()
    def remove_last_trim(self):
        self.trim_list.pop()
        self.updateTable()
    def update_initial_conditions(self):
        # fail early for impossible simulations
        if self.init_vel.value() == 0:
            raise ValueError("Must have nonzero starting velocity")
        if self.total_time.value() == 0:
            raise ValueError("Must have nonzero simulation time")
        # find_system adds delta_el and thrust
        self.initial_conditions = find_system(self.init_vel.value(), np.radians(self.init_gamma.value()))
        # add user-defined parameters to the initial_conditions
        self.initial_conditions["altitude"] = self.init_altitude.value()
        self.initial_conditions["q"] = np.radians(self.init_angvel.value())
        self.initial_conditions["t_total"] = self.total_time.value()
        self.initial_conditions["U_0"] = find_U_0(self.initial_conditions)
    def run_simulation(self):
        # get initial conditions from ui
        self.update_initial_conditions()
        # actually run the simulation
        self.sim_result = integrate_system(self.initial_conditions, self.trim_list)
        self.graph_selector.clear()
        # create a list of graphing options
        graph_selector_keys = list(find_state_parameters(self.sim_result["U"][0]).keys())
        graph_selector_keys.sort()
        self.graph_selector.addItems(graph_selector_keys)
        self.update_plot()
    def update_plot(self):
        # Check for empty selection
        if self.graph_selector.currentText() == '':
            return
        self.graph.ax.clear()
        # plot selected graph
        plot_parameter(self.graph, self.graph_selector.currentText(), self.sim_result["U"], self.sim_result["t"])
        self.graph.view.draw()
    def mainwindow(self):
        # return to main window
        self.mw = MainWindow()
        self.mw.show()
        self.hide()
    def updateTable(self):
        # add a new trim condition to the table of trim conditions
        from pprint import pprint
        if len(self.trim_list) == 0:
            self.trim_table.clear()
            return
        keys = sorted(list(self.trim_list[0].keys()))
        self.trim_table.setRowCount(len(keys))
        self.trim_table.setColumnCount(len(self.trim_list))
        self.trim_table.setVerticalHeaderLabels(keys)
        for i in range(len(keys)):
            for j in range(len(self.trim_list)):
                self.trim_table.setItem(i, j, QTableWidgetItem("{:.3f}".format(self.trim_list[j][keys[i]])))


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
        # go to main simulation window
        self.simwin = SimWindow()
        self.simwin.show()
        self.hide()

if __name__ == "__main__":
    # start the application when run
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())