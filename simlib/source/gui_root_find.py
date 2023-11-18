"Code for root finding (Question B1)"

import sys
sys.path.append('simlib')
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
)

from source.plot import param_fix_vel, param_fix_gamma, system_keys, GraphWidget
from gui_root_finder_iterables import methods, err_types
from gui.rf_mwc import Ui_MainWindow
import time

class Rf_MW(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(Rf_MW, self).__init__(parent)
        # get code from QtDesigner
        self.setupUi(self)
        # connect graphs
        self.graph = GraphWidget()
        graph_layout = QGridLayout()
        graph_layout.addWidget(self.graph)
        self.graph_output.setLayout(graph_layout)
        self.graph_selector.addItems(system_keys)
        self.method_selector.addItems(sorted(methods.keys()))
        self.err_selector.addItems(sorted(err_types))
        # connect callbacks
        self.fix_vel.toggled.connect(self.update_slider)
        self.fix_gamma.toggled.connect(self.update_slider)
        for spinBox in [self.gamma_max, self.gamma_min, self.vel_max, self.vel_min]:
            spinBox.valueChanged.connect(self.update_slider)
        self.horizontalSlider.valueChanged.connect(self.update_graph)
        self.return_btn.clicked.connect(self.mainwindow)
        self.graph_selector.currentIndexChanged.connect(self.update_graph)
        self.err_selector.currentIndexChanged.connect(self.reset_error)
        self.reset_error()
        self.update_slider()
        self.update_graph()
    def reset_error(self):
        if self.err_selector.currentText() == "nterms":
            self.err_amt.setText("1000")
        if self.err_selector.currentText() == "absolute": 
            self.err_amt.setText("1e-7")
        if self.err_selector.currentText() == "relative":
            self.err_amt.setText("1e-3")
    def update_slider(self):
        # change slider bounds and update graph
        if self.fix_vel.isChecked():
            self.horizontalSlider.setMaximum(self.vel_max.value())
            self.horizontalSlider.setMinimum(self.vel_min.value())
            self.slider_label.setText("Velocity: ")
        elif self.fix_gamma.isChecked():
            self.horizontalSlider.setMaximum(self.gamma_max.value())
            self.horizontalSlider.setMinimum(self.gamma_min.value()) 
            self.slider_label.setText("Flight Path Angle: ")
        self.update_graph()
    def update_graph(self):
        # measure elapsed time
        if self.err_selector.currentText() == "nterms":
            e = int(self.err_amt.text())
        else:
            e = float(self.err_amt.text())
        start = time.time()
        self.graph.ax.clear()
        hs = self.horizontalSlider.value()
        self.lcdNumber.display(hs)
        if self.fix_vel.isChecked():
            param_fix_vel(graphWidget=self.graph,
                param = self.graph_selector.currentText(),
                vel = hs,
                gamma_min = np.radians(self.gamma_min.value()),
                gamma_max = np.radians(self.gamma_max.value()),
                method = methods[self.method_selector.currentText()],
                err_type = self.err_selector.currentText(),
                e = e)
        elif self.fix_gamma.isChecked():
            param_fix_gamma(graphWidget=self.graph,
                param = self.graph_selector.currentText(),
                gamma = np.radians(hs),
                vel_min = self.vel_min.value(),
                vel_max = self.vel_max.value(),
                method = methods[self.method_selector.currentText()],
                err_type = self.err_selector.currentText(),
                e = e)
        self.graph.view.figure.tight_layout()
        self.graph.view.draw()
        end = time.time()
        self.elapsed_time.setText("Elapsed time: {:.6f}".format(end - start))
    def mainwindow(self):
        from main import MainWindow
        # return to main window
        self.mw = MainWindow()
        self.mw.show()
        self.hide()


if __name__=="__main__":
    # run main window for testing
    app = QApplication(sys.argv)
    window = Rf_MW()
    window.show()
    sys.exit(app.exec())

    

