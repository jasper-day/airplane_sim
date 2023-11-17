# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_climb_mw.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graph_output = QWidget(self.groupBox_2)
        self.graph_output.setObjectName(u"graph_output")

        self.verticalLayout_2.addWidget(self.graph_output)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(447, 174))

        self.verticalLayout_3.addWidget(self.textBrowser, 0, Qt.AlignHCenter)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.velocity = QDoubleSpinBox(self.groupBox)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setMinimum(30.000000000000000)
        self.velocity.setMaximum(400.000000000000000)
        self.velocity.setSingleStep(10.000000000000000)
        self.velocity.setValue(118.000000000000000)

        self.gridLayout.addWidget(self.velocity, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.final_alt = QDoubleSpinBox(self.groupBox)
        self.final_alt.setObjectName(u"final_alt")
        self.final_alt.setMinimum(100.000000000000000)
        self.final_alt.setMaximum(10000.000000000000000)
        self.final_alt.setSingleStep(200.000000000000000)
        self.final_alt.setValue(2000.000000000000000)

        self.gridLayout.addWidget(self.final_alt, 2, 1, 1, 1)

        self.climb_angle = QDoubleSpinBox(self.groupBox)
        self.climb_angle.setObjectName(u"climb_angle")
        self.climb_angle.setMinimum(-30.000000000000000)
        self.climb_angle.setMaximum(30.000000000000000)
        self.climb_angle.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.climb_angle, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.starting_alt = QDoubleSpinBox(self.groupBox)
        self.starting_alt.setObjectName(u"starting_alt")
        self.starting_alt.setMinimum(100.000000000000000)
        self.starting_alt.setMaximum(10000.000000000000000)
        self.starting_alt.setSingleStep(200.000000000000000)
        self.starting_alt.setValue(1000.000000000000000)

        self.gridLayout.addWidget(self.starting_alt, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.altitude_output = QLineEdit(self.groupBox_3)
        self.altitude_output.setObjectName(u"altitude_output")
        self.altitude_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.altitude_output, 1, 1, 1, 1)

        self.t_climb_output = QLineEdit(self.groupBox_3)
        self.t_climb_output.setObjectName(u"t_climb_output")
        self.t_climb_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.t_climb_output, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.run_btn = QPushButton(self.widget)
        self.run_btn.setObjectName(u"run_btn")

        self.verticalLayout_4.addWidget(self.run_btn)

        self.reset_btn = QPushButton(self.widget)
        self.reset_btn.setObjectName(u"reset_btn")

        self.verticalLayout_4.addWidget(self.reset_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.return_btn = QPushButton(self.widget)
        self.return_btn.setObjectName(u"return_btn")

        self.verticalLayout_3.addWidget(self.return_btn)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This section allows you to find the time it takes our airplane to climb from one height to another. To run a simulation, select the appropriate starting and ending heights and the angle at which you wish the plane to climb. The necessary length of time for the plane to fly will be calculated, and a graph of the output displayed.</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Simulation Conditions", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Climb Angle (deg)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Velocity (m/s)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Starting Altitude (m)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Final Altitude (m)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Final Altitude", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Time to Climb", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"Find climb time", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.return_btn.setText(QCoreApplication.translate("MainWindow", u"Back to Menu", None))
    # retranslateUi

