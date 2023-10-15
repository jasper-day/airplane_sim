# GUI (Graphical User Interface) for airplane sim
# Using PySide6 as a cross-platform framework (bindings for qt)

# Test that pyside is working
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton, QDialog, QLineEdit,
                               QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QGridLayout)
from PySide6.QtCore import Slot
from aero_table import alpha, delta_el, CD, CL, CM, CL_el, CM_el
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np

alpha_table = np.array([alpha, CD, CL, CM])
delta_el_table = np.array([delta_el, CL_el, CM_el])

class AlphaTable(QTableWidget):
    # QTableWidget presents tabular data in a spreadsheet-like fashion.
    # Here we present the relation between angle of attack and various coefficients
    def __init__(self, parent=None):
        super(AlphaTable, self).__init__(parent)
        self.setColumnCount(len(alpha))
        self.setRowCount(4)
        self.setVerticalHeaderLabels(["alpha", "CD", "CL", "CM"])
        self.setAlternatingRowColors(True)
        for i in range(len(alpha)):
            for j in range(4):
                self.setItem(j, i, QTableWidgetItem(str(alpha_table[j][i])))

class DeltaTable(QTableWidget):
    # QTableWidget presents tabular data in a spreadsheet-like fashion.
    # Here we present the relation between elevator angle and various coefficients
    def __init__(self, parent=None):
        super(DeltaTable, self).__init__(parent)
        self.setColumnCount(len(delta_el))
        self.setRowCount(3)
        self.setVerticalHeaderLabels(["delta_el", "CL_el", "CM_el"])
        self.setAlternatingRowColors(True)
        for i in range(len(delta_el)):
            for j in range(3):
                self.setItem(j, i, QTableWidgetItem(str(delta_el_table[j][i])))

class AlphaGraph(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=None):
        super(AlphaGraph, self).__init__(parent)
        self.resize(400, 300)
        # Figures contain axes, which plot data
        self.figure = Figure()
        # canvases contain figures and are Qt Widgets
        self.canvas = FigureCanvas(self.figure)
        # Plot the desired data
        self.ax = self.figure.add_subplot(111)
        self.ax.scatter(alpha, CD, label="CD")
        self.ax.scatter(alpha, CL, label="CL")
        self.ax.scatter(alpha, CM, label="CM")
        self.ax.set_xlabel("Angle of Attack")
        self.ax.legend()
        self.layout = QVBoxLayout(self)
        # Add the widget to the layout
        self.layout.addWidget(self.canvas)

class DeltaGraph(QWidget):
    def __init__(self, parent=None):
        super(DeltaGraph, self).__init__(parent)
        self.resize(400, 300)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        # Plot the desired data
        self.ax.scatter(delta_el, CL_el, label="CL_el")
        self.ax.scatter(delta_el, CM_el, label="CM_el")
        self.ax.set_xlabel("Elevator Deflection")
        self.ax.legend()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

class MainWindow(QMainWindow):
    # The MainWindow holds everything.
    # Here I coded everything by hand (with the help of Copilot), 
    # but in the future it would be more efficient to use pyside6-designer.exe
    # to design the layouts.
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Aero Table")
        self.resize(800, 600)
        self.alpha_table = AlphaTable()
        self.delta_table = DeltaTable()
        self.alpha_graph = AlphaGraph()
        self.delta_graph = DeltaGraph()
        self.statusBar().showMessage("Ready")
        # add tables to main window
        self._main = QWidget()
        self.setCentralWidget(self._main)
        # nested layout
        layout = QGridLayout(self._main)
        layout.addWidget(self.alpha_table, 0,0)
        layout.addWidget(self.alpha_graph, 0,1)
        layout.addWidget(self.delta_table, 1,0)
        layout.addWidget(self.delta_graph, 1,1)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
