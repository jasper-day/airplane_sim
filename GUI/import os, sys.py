import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QPushButton,
)
from Page_1 import AlphaGraph, AlphaTable, Page_Alpha
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



class tabwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Data menu")
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.alphaTabUI(), "Alpha")
        tabs.addTab(self.delta_elTabUI(), "Delta_el")
        layout.addWidget(tabs)


    def alphaTabUI(self):
        """Create the alpha page UI."""
        self.alpha_graph = AlphaGraph()
        self.alpha_table = AlphaTable()
        alphaTab = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.alpha_graph,0,0)
        layout.addWidget(self.alpha_table,1,0)
        alphaTab.setLayout(layout)
        return alphaTab

    def delta_elTabUI(self):
        """Create the del_el page UI."""
        self.delta_table = DeltaTable()
        self.delta_graph = DeltaGraph()
        delta_elTab = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.delta_graph,0,0)
        layout.addWidget(self.delta_table,1,0)
        delta_elTab.setLayout(layout)
        return delta_elTab
    
    def mainwindow(self):
        self.mw = Window()
        self.mw.show()
        self.hide()

class Window2(QMainWindow):                           # <===
    def __init__(self, parent = None):
        super(Window2, self).__init__(parent)
        self.w2_mainwidget = QWidget(self)
        self.w2_tabwidget = tabwidget(self)

        self.w2_mainlayout = QVBoxLayout(self.w2_mainwidget)
        self.w2_mainlayout.addWidget(self.w2_tabwidget)
        self.Homebutton = QPushButton("Back to Menu", self)
        self.Homebutton.clicked.connect(self.mainwindow)
        self.w2_mainlayout.addWidget(self.Homebutton)

        self.w2_mainwidget.setLayout(self.w2_mainlayout)
        self.setCentralWidget(self.w2_mainwidget)
        
    def mainwindow(self):
        self.mw = Window()
        self.mw.show()
        self.hide()


# vvvvvvvvvvvvv  Confirmed good code below  vvvvvvvvvvvvv


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout Example")
        layout = QGridLayout(self)
        
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")
        
        self.button1 = QPushButton("Start", self)
        self.button1.clicked.connect(self.window2)
        self.button2 = QPushButton("Quit",self)
        self.button2.clicked.connect(sys.exit)
        
        layout.addWidget(self.label, 0,0)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,2,0)
        self.setLayout(layout)
        
    #     # Create the stacked layout
    #     self.stackedLayout = QStackedLayout()
        
        
        
    #     # Create the first page
    #     self.page1 = QWidget()
    #     self.page1Layout = QFormLayout()
    #     self.page1Layout.addRow("Name:", QLineEdit())
    #     self.page1Layout.addRow("Address:", QLineEdit())
    #     self.page1.setLayout(self.page1Layout)
    #     self.stackedLayout.addWidget(self.page1)
        
        
    #     # Create the second page
    #     self.page2 = QWidget()
    #     self.page2Layout = QFormLayout()
    #     self.page2Layout.addRow("Job:", QLineEdit())
    #     self.page2Layout.addRow("Department:", QLineEdit())
    #     self.page2.setLayout(self.page2Layout)
    #     self.stackedLayout.addWidget(self.page2)
    #     layout.addLayout(self.stackedLayout, 0,1,3,3)

    # def switchtoPage0(self):
    #     self.stackedLayout.setCurrentIndex(0)

    # def switchtoPage1(self):
    #     self.stackedLayout.setCurrentIndex(1)

    def window2(self):
        self.w2 = Window2()
        self.w2.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
 

    window = Window()
    window.show()
    sys.exit(app.exec())