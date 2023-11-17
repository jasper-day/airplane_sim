import sys
sys.path.append('simlib/source/')
from gui.simulator_mw_testc import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QMovie, QFont
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
    def __init__(self, parent = None):
        super(SimWindow, self).__init__(parent)
        self.setupUi(self)
        self.graph = GraphWidget()
        self.graph_layout = QHBoxLayout()
        self.graph_layout.addWidget(self.graph)
        self.graph_output.setLayout(self.graph_layout)
        self.trim_list = [] # data for commands
        self.initial_conditions = {} # data for initial conditions
        self.add_trim_btn.clicked.connect(self.add_trim)
        self.del_prev_trim_btn.clicked.connect(self.remove_last_trim)
        self.clear_trims_btn.clicked.connect(self.clear_trims)
        self.run_simulation_btn.clicked.connect(self.run_simulation)
        self.update_plot_btn.clicked.connect(self.update_plot)
        self.exit_btn.clicked.connect(self.mainwindow)
        self.graph_selector.currentIndexChanged.connect(self.update_plot)
    def add_trim(self):
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
        if self.init_vel.value() == 0:
            raise ValueError("Must have nonzero starting velocity")
        if self.total_time.value() == 0:
            raise ValueError("Must have nonzero simulation time")
        self.initial_conditions = find_system(self.init_vel.value(), np.radians(self.init_gamma.value()))
        self.initial_conditions["altitude"] = self.init_altitude.value()
        self.initial_conditions["q"] = np.radians(self.init_angvel.value())
        self.initial_conditions["t_total"] = self.total_time.value()
        self.initial_conditions["U_0"] = find_U_0(self.initial_conditions)
    def run_simulation(self):
        self.update_initial_conditions()
        self.sim_result = integrate_system(self.initial_conditions, self.trim_list)
        self.graph_selector.clear()
        graph_selector_keys = list(find_state_parameters(self.sim_result["U"][0]).keys())
        graph_selector_keys.sort()
        self.graph_selector.addItems(graph_selector_keys)
        self.update_plot()
    def update_plot(self):
        self.graph.ax.clear()
        plot_parameter(self.graph, self.graph_selector.currentText(), self.sim_result["U"], self.sim_result["t"])
        self.graph.view.figure.tight_layout()
        self.graph.view.draw()
    def mainwindow(self):
        self.mw = MainWindow()
        self.mw.show()
        self.hide()
    def updateTable(self):
        from pprint import pprint
        pprint(self.trim_list)
        if len(self.trim_list) == 0:
            self.trim_table.clear()
            return
        keys = list(self.trim_list[0].keys())
        keys.sort()
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
        self.button1.setFont(QFont('ISOCP_IV50', 16))
        self.button1.clicked.connect(self.simwin)
        self.button2 = QPushButton("Quit",self)
        self.button2.setFont(QFont('ISOCP_IV50', 16))
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