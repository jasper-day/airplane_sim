import sys

sys.path.append("simlib/source/")
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
)

from source.plot import GraphWidget, plot_b2_answer
from gui.t_climb_mwc import Ui_MainWindow
from main import MainWindow

class TClimbMW(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TClimbMW, self).__init__(parent)
        self.setupUi(self)
        # add graph
        self.graph = GraphWidget()
        graph_layout = QGridLayout()
        graph_layout.addWidget(self.graph)
        self.graph_output.setLayout(graph_layout)
        # add callbacks
        self.run_btn.clicked.connect(self.run_simulation)
        self.reset_btn.clicked.connect(self.reset)
        self.return_btn.clicked.connect(self.mainwindow)
    def reset(self):
        # restore spinBoxes to default values
        self.velocity.setValue(118)
        self.starting_alt.setValue(1000)
        self.final_alt.setValue(2000)
        self.climb_angle.setValue(2)
    def run_simulation(self):
        self.graph.ax.clear()
        # plot answer and get result
        res = plot_b2_answer(
            self.graph,
            velocity=self.velocity.value(),
            starting_alt=self.starting_alt.value(),
            final_alt=self.final_alt.value(),
            climb_angle=np.radians(self.climb_angle.value()),
        )
        self.graph.view.figure.tight_layout()
        self.graph.view.draw()
        self.t_climb_output.setText("{:.2f}".format(res["t_climb"]))
        self.altitude_output.setText("{:.2f}".format(res["final_alt"]))
    def mainwindow(self):
        # return to main window
        self.mw = MainWindow()
        self.mw.show()
        self.hide()


if __name__ == "__main__":
    # run main window for testing
    app = QApplication(sys.argv)
    window = TClimbMW()
    window.show()
    sys.exit(app.exec())
