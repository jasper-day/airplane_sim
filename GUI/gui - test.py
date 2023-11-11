import sys
sys.path.append(r'C:\Users\thoma\OneDrive - University of Edinburgh\Year 3\Computational Methods and Modelling 3\airplane_sim')
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import QSize
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
)
from aero_table import alpha, delta_el, CD, CL, CM, CL_el, CM_el
from displaytable import Velocity, Gamma, Alpha, dE, Thrust, Duration
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

data = [Velocity, Gamma, Alpha, dE, Thrust, Duration]

class TestGraph(QWidget):
    # Matplotlib graphs can be widgets too.
    def __init__(self, parent=None):
        super(TestGraph, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax1 = self.figure.add_subplot(421)
        self.ax2 = self.figure.add_subplot(422)
        self.ax3 = self.figure.add_subplot(423)
        self.ax4 = self.figure.add_subplot(424)
        self.ax5 = self.figure.add_subplot(425)
        self.ax6 = self.figure.add_subplot(426)
        self.ax7 = self.figure.add_subplot(427)
        self.ax8 = self.figure.add_subplot(428)
        # Plot the desired data
        self.ax1.scatter(delta_el, CL_el, label="CL_el", color="C4")
        self.ax2.scatter(delta_el, CM_el, label="CM_el", color="C5")
        self.ax3.scatter(delta_el, CL_el, label="CL_el", color="C4")
        self.ax4.scatter(delta_el, CM_el, label="CM_el", color="C5")
        self.ax5.scatter(delta_el, CL_el, label="CL_el", color="C4")
        self.ax6.scatter(delta_el, CM_el, label="CM_el", color="C5")
        self.ax7.scatter(delta_el, CL_el, label="CL_el", color="C4")
        self.ax8.scatter(delta_el, CM_el, label="CM_el", color="C5")

        self.ax1.set_xlabel("Elevator Deflection")
        self.ax2.set_xlabel("Elevator Deflection")
        self.ax3.set_xlabel("Elevator Deflection")
        self.ax4.set_xlabel("Elevator Deflection")
        self.ax5.set_xlabel("Elevator Deflection")
        self.ax6.set_xlabel("Elevator Deflection")
        self.ax7.set_xlabel("Elevator Deflection")
        self.ax8.set_xlabel("Elevator Deflection")

        self.ax1.legend()
        self.ax2.legend()
        self.ax3.legend()
        self.ax4.legend()
        self.ax5.legend()
        self.ax6.legend()
        self.ax7.legend()
        self.ax8.legend()

        # Figure.tight_layout(self.figure)
        Figure.tight_layout(self.figure,h_pad=-1)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)


class TestTable(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget(self)
        self.setupTable()
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.velo_label = QLabel("Velocity: ")
        self.velo_input = QLineEdit()
        self.velo_input.setPlaceholderText('Please enter the velocity')
        self.gamma_input = QLineEdit()
        self.gamma_input.setPlaceholderText('Please enter the flight path angle')
        self.dur_input = QLineEdit()
        self.dur_input.setPlaceholderText('Please enter the duration')

        self.addbutton = QPushButton('Add Condition', self)
        self.addbutton.clicked.connect(self.addData)
        self.addbutton.clicked.connect(self.refreshTable)
        self.clearbutton = QPushButton('Clear', self)
        self.clearbutton.setFixedHeight(54)
        self.clearbutton.clicked.connect(self.clearTable)
        self.runbutton = QPushButton('Run', self)
        self.runbutton.setFixedHeight(54)
        
        layout = QGridLayout(self)
        layout.addWidget(self.tableWidget,0,0,1,2)
        layout.addWidget(self.velo_label,1,0)
        layout.addWidget(self.velo_input,1,1)
        layout.addWidget(self.runbutton,1,1,2,1)
        layout.addWidget(self.gamma_input,2,0)
        layout.addWidget(self.dur_input,3,0)
        layout.addWidget(self.clearbutton,3,1,2,1)
        layout.addWidget(self.addbutton,4,0)

    def setupTable(self):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setVerticalHeaderLabels(['Velocity', 'Gamma', 'Alpha', 'dE', 'Thrust', 'Duration'])

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))


    def addData(self):
        data[0].append(int(self.velo_input.text()))
        data[1].append(int(self.gamma_input.text()))
        data[2].append(int(self.dur_input.text()))

    def refreshTable(self):
        # Clear the existing items in the table
        self.tableWidget.clear()
        # Setup the table again with updated data
        self.setupTable()

    def clearTable(self):
        data[0].clear()
        data[1].clear()
        data[2].clear()
        self.tableWidget.clear()
        self.setupTable()   
    

class plane(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.movie.setScaledSize(QSize(600,200))
        self.movie.start()

        self.label.setMovie(self.movie)
        # self.label.setMinimumSize(self.movie.scaledSize()
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")


class Window2(QMainWindow):                           
    def __init__(self, parent = None):
        super(Window2, self).__init__(parent)
        self.setWindowTitle("SimuPlane™ 0.1.0")
        self.resize(1200,800)
        self.w2_mainwidget = QWidget(self)
        self.w2_mainlayout = QHBoxLayout()
        self.w2_Llayout = QGridLayout()
        self.w2_Rlayout = QGridLayout()
        
        #Defining graph
        self.graph = TestGraph()
        #Defining graphics
        self.plane = plane()
        #Defining table
        self.table = TestTable()

        #Add home button
        self.homebutton = QPushButton("Back to Menu", self)
        self.homebutton.clicked.connect(self.mainwindow)

        #Populating left layout
        self.w2_Llayout.addWidget(self.graph,0,0,3,1)
        self.w2_Llayout.addWidget(self.homebutton,3,0)

        #Populating right layout
        self.w2_Rlayout.addWidget(self.plane,0,0,3,1)
        self.w2_Rlayout.addWidget(self.table,3,0,2,1)

        #Adding sublayouts to main layout
        self.w2_mainlayout.addLayout(self.w2_Llayout)
        self.w2_mainlayout.addLayout(self.w2_Rlayout)

        #Setting main layout
        self.w2_mainwidget.setLayout(self.w2_mainlayout)
        self.setCentralWidget(self.w2_mainwidget)
        
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
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")
        
        self.button1 = QPushButton("Start", self)
        self.button1.clicked.connect(self.window2)
        self.button2 = QPushButton("Quit",self)
        self.button2.clicked.connect(sys.exit)
        
        layout.addWidget(self.label, 0,0)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,2,0)
        self.setLayout(layout)

    def window2(self):
        self.w2 = Window2()
        self.w2.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
 

    window = MainWindow()
    window.show()
    sys.exit(app.exec())