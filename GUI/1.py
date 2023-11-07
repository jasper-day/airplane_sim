import sys
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QMovie
from Page_1 import AlphaGraph, AlphaTable, Page_Alpha
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QCheckBox,
    QTabWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QStackedLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QSizePolicy,
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

class Mainmenu(QWidget):
    
    def setupUI(self, Main):

        Main.setObjectName("SimuPlane™ 0.1.0")
        Main.setFixedSize(1440, 900)

        self.width = 1440
        self.height = 900

        self.resize(self.width, self.height)

        self.menu = QStackedLayout()

        self.mainmenu = QWidget()
        self.datamenu = QWidget()

        self.mainmenuUI()
        self.datamenuUI()

        self.menu.addWidget(self.mainmenu)
        self.menu.addWidget(self.datamenu)

    def mainmenuUI(self):

        QWidget.startmenu(self)
        self.setWindowTitle("SimuPlane™ 0.1.0")
        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")

        self.button = QPushButton("Start", self)
        self.button1 = QPushButton("Quit",self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addWidget(self.button1, 2, 0)
        

        self.setLayout(self.layout)
        self.show()


    def datamenuUI(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Example")
        self.resize(1440, 900)
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

class MainWindow(QMainWindow,Mainmenu):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("SimuPlane™ 0.1.0")

        self.setupUI(self)

        self.button.clicked.connect(self.???)
        self.button1.clicked.connect(self.datamenu)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTabWidget Example")
#         self.resize(1440, 900)
#         # Create a top-level layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         # Create the tab widget with two tabs
#         tabs = QTabWidget()
#         tabs.addTab(self.alphaTabUI(), "Alpha")
#         tabs.addTab(self.delta_elTabUI(), "Delta_el")
#         layout.addWidget(tabs)


#     def alphaTabUI(self):
#         """Create the alpha page UI."""
#         self.alpha_graph = AlphaGraph()
#         self.alpha_table = AlphaTable()
#         alphaTab = QWidget()
#         layout = QGridLayout()
#         layout.addWidget(self.alpha_graph,0,0)
#         layout.addWidget(self.alpha_table,1,0)
#         alphaTab.setLayout(layout)
#         return alphaTab

#     def delta_elTabUI(self):
#         """Create the del_el page UI."""
#         self.delta_table = DeltaTable()
#         self.delta_graph = DeltaGraph()
#         delta_elTab = QWidget()
#         layout = QGridLayout()
#         layout.addWidget(self.delta_graph,0,0)
#         layout.addWidget(self.delta_table,1,0)
#         delta_elTab.setLayout(layout)
#         return delta_elTab

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())



# Code for main menu tab
# tabs.addTab(self.MainTabUI(MainWindow=0), "Main Menu")

#     def MainTabUI(self, MainWindow):
#         """Create the main page UI."""
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(250, 250)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         maintab = QWidget()
#         layout = QGridLayout()
#         label = QLabel()
#         movie = QMovie('p51_3d.gif')
#         label.setMovie(movie)
#         movie.start()
#         return maintab






# class Mainmenu(QWidget):
    
#     def startmenu(self):
#         QWidget.startmenu(self)
#         self.setWindowTitle("SimuPlane™ 0.1.0")
#         # Define a label for displaying GIF
#         self.label = QtWidgets.QLabel(self)

#         # Integrate QMovie to the label and initiate the GIF
#         self.movie = QMovie("p51_3d.gif")
#         self.label.setMovie(self.movie)
#         self.movie.start()

#         self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
#         self.label.setStyleSheet("QLabel {background-color: white;}")

#         self.button = QPushButton("Start", self)
#         self.button1 = QPushButton("Quit",self)

#         self.layout = QGridLayout()
#         self.layout.addWidget(self.label, 0, 0)
#         self.layout.addWidget(self.button, 1, 0)
#         self.layout.addWidget(self.button1, 2, 0)
        

#         self.setLayout(self.layout)
#         self.show()