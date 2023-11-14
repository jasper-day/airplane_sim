# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulator_mw.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.graph_output = QWidget(self.widget)
        self.graph_output.setObjectName(u"graph_output")

        self.verticalLayout_5.addWidget(self.graph_output)

        self.graph_selector = QComboBox(self.widget)
        self.graph_selector.setObjectName(u"graph_selector")

        self.verticalLayout_5.addWidget(self.graph_selector)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.movie = QWidget(self.centralwidget)
        self.movie.setObjectName(u"movie")

        self.verticalLayout_4.addWidget(self.movie)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.trim_table = QTableView(self.centralwidget)
        self.trim_table.setObjectName(u"trim_table")

        self.verticalLayout_3.addWidget(self.trim_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.init_vel = QDoubleSpinBox(self.groupBox_3)
        self.init_vel.setObjectName(u"init_vel")

        self.horizontalLayout_4.addWidget(self.init_vel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.init_gamma = QDoubleSpinBox(self.groupBox_3)
        self.init_gamma.setObjectName(u"init_gamma")

        self.horizontalLayout_5.addWidget(self.init_gamma)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.init_angvel = QDoubleSpinBox(self.groupBox_3)
        self.init_angvel.setObjectName(u"init_angvel")

        self.horizontalLayout_6.addWidget(self.init_angvel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.init_altitude = QDoubleSpinBox(self.groupBox_3)
        self.init_altitude.setObjectName(u"init_altitude")

        self.horizontalLayout_7.addWidget(self.init_altitude)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.init_total_time = QDoubleSpinBox(self.groupBox_3)
        self.init_total_time.setObjectName(u"init_total_time")

        self.horizontalLayout_8.addWidget(self.init_total_time)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.trim_vel = QDoubleSpinBox(self.groupBox)
        self.trim_vel.setObjectName(u"trim_vel")

        self.horizontalLayout.addWidget(self.trim_vel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.trim_gamma = QDoubleSpinBox(self.groupBox)
        self.trim_gamma.setObjectName(u"trim_gamma")

        self.horizontalLayout_2.addWidget(self.trim_gamma)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.trim_time_start = QDoubleSpinBox(self.groupBox)
        self.trim_time_start.setObjectName(u"trim_time_start")

        self.horizontalLayout_3.addWidget(self.trim_time_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.add_trim_btn = QPushButton(self.groupBox)
        self.add_trim_btn.setObjectName(u"add_trim_btn")

        self.verticalLayout.addWidget(self.add_trim_btn)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.del_prev_trim_btn = QPushButton(self.groupBox)
        self.del_prev_trim_btn.setObjectName(u"del_prev_trim_btn")

        self.horizontalLayout_9.addWidget(self.del_prev_trim_btn)

        self.clear_trims_btn = QPushButton(self.groupBox)
        self.clear_trims_btn.setObjectName(u"clear_trims_btn")

        self.horizontalLayout_9.addWidget(self.clear_trims_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.run_simulation_btn = QPushButton(self.centralwidget)
        self.run_simulation_btn.setObjectName(u"run_simulation_btn")

        self.verticalLayout_4.addWidget(self.run_simulation_btn)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back to Menu", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Initial Conditions", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocity (m/s)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Flight Path Angle (\u00b0)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity (\u00b0/s)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Altitude (m)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Simulation time (s)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Velocity (m/s)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Flight Path Angle (\u00b0)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Starting Time (s)", None))
        self.add_trim_btn.setText(QCoreApplication.translate("MainWindow", u"Add Trim", None))
        self.del_prev_trim_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Prev", None))
        self.clear_trims_btn.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.run_simulation_btn.setText(QCoreApplication.translate("MainWindow", u"Run Simulation", None))
    # retranslateUi

