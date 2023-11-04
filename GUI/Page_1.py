# GUI (Graphical User Interface) for airplane sim
# Using PySide6 as a cross-platform framework (bindings for qt)

# Test that pyside is working
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton, QDialog, QLineEdit,
                               QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QGridLayout)
from PySide6.QtCore import Slot
# from PySide6 import uic
from aero_table import alpha, CD, CL, CM
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np

alpha_table = np.array([alpha, CD, CL, CM])

class AlphaTable(QTableWidget):
    # QTableWidget presents tabular data in a spreadsheet-like fashion.
    # Here we present the relation between angle of attack and various coefficients
    def __init__(self, parent=None):
        super(AlphaTable, self).__init__(parent)
        # self.resize(400, 500)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["alpha", "CD", "CL", "CM"])
        self.setRowCount(len(alpha))
        self.setAlternatingRowColors(True)
        for i in range(len(alpha)):
            for j in range(4):
                self.setItem(j, i, QTableWidgetItem(str(alpha_table[j][i])))

class AlphaGraph(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=None):
        super(AlphaGraph, self).__init__(parent)
        # self.resize(400, 300)
        # Figures contain axes, which plot data
        self.figure = Figure()
        # canvases contain figures and are Qt Widgets
        self.canvas = FigureCanvas(self.figure)
        # Plot the desired data
        # Three separate subplots
        self.ax1 = self.figure.add_subplot(131)
        self.ax2 = self.figure.add_subplot(132)
        self.ax3 = self.figure.add_subplot(133)
        self.ax1.scatter(alpha, CD, label="CD", color="C1")
        self.ax2.scatter(alpha, CL, label="CL", color="C2")
        self.ax3.scatter(alpha, CM, label="CM", color="C3")
        self.ax1.set_xlabel("Angle of Attack")
        self.ax2.set_xlabel("Angle of Attack")
        self.ax3.set_xlabel("Angle of Attack")
        self.ax1.legend()
        self.ax2.legend()
        self.ax3.legend()
        Figure.tight_layout(self.figure)
        self.layout = QVBoxLayout(self)
        # Add the widget to the layout
        self.layout.addWidget(self.canvas)

class Page_Alpha(QMainWindow):
    # The MainWindow holds everything.
    # Here I coded everything by hand (with the help of Copilot), 
    # but in the future it would be more efficient to use pyside6-designer.exe
    # to design the layouts.
    def __init__(self, parent=None):
        super(Page_Alpha, self).__init__(parent)
        self.setWindowTitle("Aero Table")
        self.resize(1200, 900)
        self.alpha_table = AlphaTable()
        self.alpha_graph = AlphaGraph()
        self.statusBar().showMessage("Ready")
        # add tables to main window
        self._main = QWidget()
        self.setCentralWidget(self._main)
        # nested layout
        layout = QGridLayout(self._main)
        layout.setColumnMinimumWidth(0,425)
        layout.setColumnMinimumWidth(1,900)
        layout.setRowMinimumHeight(0,400)
        layout.addWidget(self.alpha_table, 0,0)
        layout.addWidget(self.alpha_graph, 0,1)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Page_Alpha()
    mainWin.show()
    sys.exit(app.exec())
