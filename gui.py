# GUI (Graphical User Interface) for airplane sim
# Using PySide6 as a cross-platform framework (bindings for qt)

# Test that pyside is working

import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QTabWidget,
    QStackedWidget,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
)
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
        Figure.tight_layout(self.figure,pad=0.5,w_pad=-1.5)
        self.layout = QVBoxLayout(self)
        # Add the widget to the layout
        self.layout.addWidget(self.canvas)

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

class DeltaGraph(QWidget):
    def __init__(self, parent=None):
        super(DeltaGraph, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax1 = self.figure.add_subplot(121)
        self.ax2 = self.figure.add_subplot(122)
        # Plot the desired data
        self.ax1.scatter(delta_el, CL_el, label="CL_el", color="C4")
        self.ax2.scatter(delta_el, CM_el, label="CM_el", color="C5")
        self.ax1.set_xlabel("Elevator Deflection")
        self.ax2.set_xlabel("Elevator Deflection")
        self.ax1.legend()
        self.ax2.legend()
        Figure.tight_layout(self.figure)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

class Widget1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("SimuPlane™ 0.1.0")

        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(self)
        self.setMinimumSize(QtCore.QSize(1200, 800))

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")

        self.button = QPushButton("Start", self)
        self.button.setMinimumSize(QtCore.QSize(500, 80))
        self.button.clicked.connect(self.switch_widget)
        self.button1 = QPushButton("Quit",self)
        self.button1.setMinimumSize(QtCore.QSize(500, 80))

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addWidget(self.button1, 2, 0)

        self.setLayout(self.layout)
 
    def switch_widget(self):
        stacked_widget.setCurrentIndex(1)
 
 
class Widget2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Data menu")
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.alphaTabUI(), "Alpha")
        tabs.addTab(self.delta_elTabUI(), "Delta_el")
        layout.addWidget(tabs)


    def alphaTabUI(self):
        """Create the alpha page UI."""
        self.alpha_graph = AlphaGraph()
        self.alpha_table = AlphaTable()
        self.button = QPushButton("Back to Menu", self)
        self.button.clicked.connect(self.switch_widget)
        alphaTab = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.alpha_graph,0,0)
        layout.addWidget(self.alpha_table,1,0)
        layout.addWidget(self.button,2,0)
        alphaTab.setLayout(layout)
        return alphaTab

    def delta_elTabUI(self):
        """Create the del_el page UI."""
        self.delta_table = DeltaTable()
        self.delta_graph = DeltaGraph()
        self.button = QPushButton("Back to Menu", self)
        self.button.clicked.connect(self.switch_widget)
        delta_elTab = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.delta_graph,0,0)
        layout.addWidget(self.delta_table,1,0)
        layout.addWidget(self.button,2,0)
        delta_elTab.setLayout(layout)
        return delta_elTab
        
 
    def switch_widget(self):
        stacked_widget.setCurrentIndex(0)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    # Create the QStackedWidget and add the two widgets to it
    stacked_widget = QStackedWidget()
    widget1 = Widget1()
    widget2 = Widget2()
    stacked_widget.addWidget(widget1)
    stacked_widget.addWidget(widget2)
 
    # Show the first widget
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()
 
    sys.exit(app.exec())




# import sys
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow,
#     QPushButton, QDialog, QLineEdit,
#     QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QGridLayout)
# from PySide6.QtCore import Slot
# from aero_table import alpha, delta_el, CD, CL, CM, CL_el, CM_el
# from matplotlib.backends.backend_qtagg import FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np

# alpha_table = np.array([alpha, CD, CL, CM])
# delta_el_table = np.array([delta_el, CL_el, CM_el])

# class AlphaTable(QTableWidget):
#     # QTableWidget presents tabular data in a spreadsheet-like fashion.
#     # Here we present the relation between angle of attack and various coefficients
#     def __init__(self, parent=None):
#         super(AlphaTable, self).__init__(parent)
#         self.setColumnCount(len(alpha))
#         self.setRowCount(4)
#         self.setVerticalHeaderLabels(["alpha", "CD", "CL", "CM"])
#         self.setAlternatingRowColors(True)
#         for i in range(len(alpha)):
#             for j in range(4):
#                 self.setItem(j, i, QTableWidgetItem(str(alpha_table[j][i])))

# class DeltaTable(QTableWidget):
#     # QTableWidget presents tabular data in a spreadsheet-like fashion.
#     # Here we present the relation between elevator angle and various coefficients
#     def __init__(self, parent=None):
#         super(DeltaTable, self).__init__(parent)
#         self.setColumnCount(len(delta_el))
#         self.setRowCount(3)
#         self.setVerticalHeaderLabels(["delta_el", "CL_el", "CM_el"])
#         self.setAlternatingRowColors(True)
#         for i in range(len(delta_el)):
#             for j in range(3):
#                 self.setItem(j, i, QTableWidgetItem(str(delta_el_table[j][i])))

# class AlphaGraph(QWidget):
#     # Matplotlib graphs can be widgets too.
#     def __init__(self, parent=None):
#         super(AlphaGraph, self).__init__(parent)
#         self.resize(400, 300)
#         # Figures contain axes, which plot data
#         self.figure = Figure()
#         # canvases contain figures and are Qt Widgets
#         self.canvas = FigureCanvas(self.figure)
#         # Plot the desired data
#         # Three separate subplots
#         self.ax1 = self.figure.add_subplot(131)
#         self.ax2 = self.figure.add_subplot(132)
#         self.ax3 = self.figure.add_subplot(133)
#         self.ax1.scatter(alpha, CD, label="CD", color="C1")
#         self.ax2.scatter(alpha, CL, label="CL", color="C2")
#         self.ax3.scatter(alpha, CM, label="CM", color="C3")
#         self.ax1.set_xlabel("Angle of Attack")
#         self.ax2.set_xlabel("Angle of Attack")
#         self.ax3.set_xlabel("Angle of Attack")
#         self.ax1.legend()
#         self.ax2.legend()
#         self.ax3.legend()
#         self.layout = QVBoxLayout(self)
#         # Add the widget to the layout
#         self.layout.addWidget(self.canvas)

# class DeltaGraph(QWidget):
#     def __init__(self, parent=None):
#         super(DeltaGraph, self).__init__(parent)
#         self.resize(400, 300)
#         self.figure = Figure()
#         self.canvas = FigureCanvas(self.figure)
#         self.ax1 = self.figure.add_subplot(121)
#         self.ax2 = self.figure.add_subplot(122)
#         # Plot the desired data
#         self.ax1.scatter(delta_el, CL_el, label="CL_el", color="C4")
#         self.ax2.scatter(delta_el, CM_el, label="CM_el", color="C5")
#         self.ax1.set_xlabel("Elevator Deflection")
#         self.ax2.set_xlabel("Elevator Deflection")
#         self.ax1.legend()
#         self.ax2.legend()
#         self.layout = QVBoxLayout(self)
#         self.layout.addWidget(self.canvas)

# class MainWindow(QMainWindow):
#     # The MainWindow holds everything.
#     # Here I coded everything by hand (with the help of Copilot), 
#     # but in the future it would be more efficient to use pyside6-designer.exe
#     # to design the layouts.
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("Aero Table")
#         self.resize(800, 600)
#         self.alpha_table = AlphaTable()
#         self.delta_table = DeltaTable()
#         self.alpha_graph = AlphaGraph()
#         self.delta_graph = DeltaGraph()
#         self.statusBar().showMessage("Ready")
#         # add tables to main window
#         self._main = QWidget()
#         self.setCentralWidget(self._main)
#         # nested layout
#         layout = QGridLayout(self._main)
#         layout.addWidget(self.alpha_table, 0,0)
#         layout.addWidget(self.alpha_graph, 0,1)
#         layout.addWidget(self.delta_table, 1,0)
#         layout.addWidget(self.delta_graph, 1,1)
        
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec())
