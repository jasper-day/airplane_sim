import sys
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
from Controller import find_command_fn, integrate_system, make_sample_plot
import source.env
from source.dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters 
from source.root_finder import find_system
from source.aero_table import alpha, delta_el, CD, CL, CM, CL_el, CM_el
from source.userinput import Tstart, Velocity, Gamma, Duration
from source.para_out import Alpha, deltaE, Thrust
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

input = [Tstart, Velocity, Gamma, Duration]
output = [Alpha, deltaE, Thrust]

V = np.array(Velocity)
G = np.array(Gamma)
t = np.array(Duration)
A = np.array(Alpha)
dE = np.array(deltaE)
t = np.array(Thrust)


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
    
    # def __init__(self, parent=None):
    #     super(TestGraph, self).__init__(parent)
    #     fig, axs = plt.subplots(4,2) 
    #     self.figure = make_sample_plot(fig,axs)
    #     self.canvas = FigureCanvas(self.figure)
    #     Figure.tight_layout(self.figure)
    #     # Figure.tight_layout(self.figure,h_pad=-1)
    #     self.layout = QVBoxLayout(self)
    #     self.layout.addWidget(self.canvas)
        

class TestTable(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget(self)
        self.tableWidget2 = QTableWidget(self)
        self.setupTable()
        self.setupTable2()
        self.setMaximumWidth(600)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.tableWidget2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.table_label = QLabel('User inputs')
        self.table2_label = QLabel('Output Parameters')

        self.tstart_label = QLabel('Condition Start n/ time')
        self.tstart_input = QLineEdit()
        self.tstart_input.setPlaceholderText('Please enter the condition start time')
        self.velo_label = QLabel('Velocity (ms<sup>−1</sup>)')
        self.velo_input = QLineEdit()
        self.velo_input.setPlaceholderText('Please enter the velocity')
        self.gamma_label = QLabel('Gamma (°)')
        self.gamma_input = QLineEdit()
        self.gamma_input.setPlaceholderText('Please enter the flight path angle')
        self.dur_label = QLabel('Duration (s)')
        self.dur_input = QLineEdit()
        self.dur_input.setPlaceholderText('Please enter the duration')

        self.inputbutton = QPushButton('Add Condition', self)
        self.inputbutton.clicked.connect(self.addData)
        self.inputbutton.clicked.connect(self.refreshTable)
        self.inputbutton.setFixedHeight(54)
        self.runbutton = QPushButton('Run', self)
        self.deletebutton = QPushButton('Delete Last',self)
        self.deletebutton.setFixedHeight(54)
        self.deletebutton.clicked.connect(self.deletelast)
        self.clearbutton = QPushButton('Clear', self)
        self.clearbutton.clicked.connect(self.clearTable)

        #Button for testing stuff
        self.testbutton = QPushButton('Test', self)
        self.testbutton.setFixedHeight(30)
        self.testbutton.clicked.connect(self.runsim)
        
        layout = QGridLayout(self)
        layout.addWidget(self.tableWidget,0,0,1,3)
        layout.addWidget(self.tableWidget2,1,0,1,3)
        layout.addWidget(self.tstart_label,2,0)
        layout.addWidget(self.tstart_input,2,1)
        layout.addWidget(self.inputbutton,2,2,2,1)
        layout.addWidget(self.velo_label,3,0)
        layout.addWidget(self.velo_input,3,1)
        layout.addWidget(self.gamma_label,4,0)
        layout.addWidget(self.gamma_input,4,1)
        layout.addWidget(self.deletebutton,4,2,2,1)
        layout.addWidget(self.dur_label,5,0)
        layout.addWidget(self.dur_input,5,1)
        layout.addWidget(self.clearbutton,6,2)
        layout.addWidget(self.runbutton,6,0,1,2)
        layout.addWidget(self.testbutton,7,0,1,3)

    def setupTable(self):
        self.tableWidget.setRowCount(len(input))
        self.tableWidget.setColumnCount(len(input[0]))
        self.tableWidget.setVerticalHeaderLabels(['Start time', 'Velocity', 'Gamma', 'Duration'])

        for i, row in enumerate(input):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

    def setupTable2(self):
        self.tableWidget2.setRowCount(len(output))
        self.tableWidget2.setColumnCount(len(output[0]))
        self.tableWidget2.setVerticalHeaderLabels(['Alpha', 'dE', 'Thrust'])

        for i, row in enumerate(output):
            for j, item in enumerate(row):
                self.tableWidget2.setItem(i, j, QTableWidgetItem(str(item)))


    def addData(self):
        input[0].append(int(self.tstart_input.text()))
        input[1].append(int(self.velo_input.text()))
        input[2].append(int(self.gamma_input.text()))
        input[3].append(int(self.dur_input.text()))
        print(input)

    def trimcond(self):
        inputnp = np.array([input[0],input[1],input[2],input[3]])
        print(f'The inputnp is: {inputnp}')
        trim_conditions = {
            "1": find_system(float(inputnp[1,0]), float(inputnp[2,0])), # steady level flight
            "2": find_system(float(inputnp[1,1]), deg2rad(float(inputnp[2,1]))), # climbing flight
            "3": find_system(float(inputnp[1,2]), float(inputnp[2,2])), # steady level flight
        }
        print(trim_conditions['1'])
        return trim_conditions   


    def total_time(self):
        total_time = sum(input[3])
        return total_time

    def timestep(self):
        timestep = 0.1
        return timestep

    def calcTrim(self):
        # trim_conditions = {
        #     "1": find_system(float(inputnp[0,0]), float(inputnp[1,0])), # steady level flight
        #     "2": find_system(float(inputnp[0,1]), deg2rad(float(inputnp[1,1]))), # climbing flight
        #     "3": find_system(float(inputnp[0,2]), float(inputnp[1,2])), # steady level flight
        # }

        find_command_fn(self.trimcond(), input[0], self.total_time(), self.timestep())

        # return trim_conditions
    
    def runsim(self):
        U_0_cond = self.trimcond()['1']
        print(U_0_cond)
        U_i = integrate_system(self.trimcond, input[0], self.total_time(), self.timestep())
        from pprint import pformat
        print(f"""
        Initial system: {pformat(find_system_parameters(U_i['U'][0]))}
        Initial commands: {pformat(self.trimcond['1'])}
        """)

    def refreshTable(self):
        # Clear the existing items in the table
        self.tableWidget.clear()
        # Setup the table again with updated data
        self.setupTable()

    def deletelast(self):
        input[0].pop()
        input[1].pop()
        input[2].pop()
        input[3].pop()
        self.tableWidget.clear()
        self.setupTable()

    def clearTable(self):
        input[0].clear()
        input[1].clear()
        input[2].clear()
        input[3].clear()
        print(f'input: {input}')
        output[0].clear()
        output[1].clear()
        output[2].clear()
        print(f'output is: {output}')
        self.tableWidget.clear()
        self.tableWidget2.clear()
        self.setupTable()
        self.setupTable2()   
    

class plane(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("simlib/p51_3d.gif")
        self.movie.setScaledSize(QSize(400,400))
        self.resize(QSize(600,400))
        self.movie.start()

        self.label.setMovie(self.movie)
        self.label.setMinimumSize(self.movie.scaledSize())
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: white}")


class Window2(QMainWindow):                           
    def __init__(self, parent = None):
        super(Window2, self).__init__(parent)
        self.setWindowTitle("SimuPlane™ 0.1.0")
        self.resize(1400,800)
        self.w2_mainwidget = QWidget(self)
        self.w2_mainlayout = QGridLayout()
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
        self.w2_mainlayout.addLayout(self.w2_Llayout,0,0)
        self.w2_mainlayout.addLayout(self.w2_Rlayout,0,1)

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
        self.movie = QMovie("simlib/p51_3d.gif")
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