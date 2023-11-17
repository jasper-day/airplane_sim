# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulator_mw_test.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        font = QFont()
        font.setFamilies([u"ISOCP_IV50"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"appicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"appicon.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.trim_table = QTableWidget(self.centralwidget)
        self.trim_table.setObjectName(u"trim_table")
        self.trim_table.setMinimumSize(QSize(0, 260))
        self.trim_table.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"ISOCP_IV50"])
        font1.setPointSize(11)
        self.trim_table.setFont(font1)

        self.verticalLayout_3.addWidget(self.trim_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(1000, 16777215))
        font2 = QFont()
        font2.setFamilies([u"ISOCP_IV50"])
        font2.setPointSize(16)
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.init_vel = QDoubleSpinBox(self.groupBox_3)
        self.init_vel.setObjectName(u"init_vel")
        self.init_vel.setFont(font1)
        self.init_vel.setCursor(QCursor(Qt.IBeamCursor))
        self.init_vel.setMaximum(400.000000000000000)
        self.init_vel.setSingleStep(10.000000000000000)
        self.init_vel.setValue(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.init_vel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.init_gamma = QDoubleSpinBox(self.groupBox_3)
        self.init_gamma.setObjectName(u"init_gamma")
        self.init_gamma.setFont(font1)
        self.init_gamma.setCursor(QCursor(Qt.IBeamCursor))
        self.init_gamma.setMinimum(-30.000000000000000)
        self.init_gamma.setMaximum(30.000000000000000)

        self.horizontalLayout_5.addWidget(self.init_gamma)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.init_angvel = QDoubleSpinBox(self.groupBox_3)
        self.init_angvel.setObjectName(u"init_angvel")
        self.init_angvel.setFont(font1)
        self.init_angvel.setCursor(QCursor(Qt.IBeamCursor))
        self.init_angvel.setMinimum(-100.000000000000000)
        self.init_angvel.setMaximum(100.000000000000000)

        self.horizontalLayout_6.addWidget(self.init_angvel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.init_altitude = QDoubleSpinBox(self.groupBox_3)
        self.init_altitude.setObjectName(u"init_altitude")
        self.init_altitude.setFont(font1)
        self.init_altitude.setCursor(QCursor(Qt.IBeamCursor))
        self.init_altitude.setMaximum(100000.000000000000000)
        self.init_altitude.setSingleStep(200.000000000000000)
        self.init_altitude.setValue(1000.000000000000000)

        self.horizontalLayout_7.addWidget(self.init_altitude)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.total_time = QDoubleSpinBox(self.groupBox_3)
        self.total_time.setObjectName(u"total_time")
        self.total_time.setFont(font1)
        self.total_time.setCursor(QCursor(Qt.IBeamCursor))
        self.total_time.setMaximum(10000.000000000000000)
        self.total_time.setSingleStep(20.000000000000000)
        self.total_time.setValue(500.000000000000000)

        self.horizontalLayout_8.addWidget(self.total_time)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(1000, 16777215))
        self.groupBox.setFont(font2)
        self.groupBox.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.run_simulation_btn = QPushButton(self.groupBox)
        self.run_simulation_btn.setObjectName(u"run_simulation_btn")
        font3 = QFont()
        font3.setFamilies([u"ISOCP_IV50"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(True)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.run_simulation_btn.setFont(font3)
        self.run_simulation_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.run_simulation_btn, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.trim_vel = QDoubleSpinBox(self.groupBox)
        self.trim_vel.setObjectName(u"trim_vel")
        self.trim_vel.setFont(font1)
        self.trim_vel.setCursor(QCursor(Qt.IBeamCursor))
        self.trim_vel.setMaximum(400.000000000000000)
        self.trim_vel.setSingleStep(10.000000000000000)
        self.trim_vel.setValue(100.000000000000000)

        self.horizontalLayout.addWidget(self.trim_vel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.trim_gamma = QDoubleSpinBox(self.groupBox)
        self.trim_gamma.setObjectName(u"trim_gamma")
        self.trim_gamma.setFont(font1)
        self.trim_gamma.setCursor(QCursor(Qt.IBeamCursor))
        self.trim_gamma.setMinimum(-30.000000000000000)
        self.trim_gamma.setMaximum(30.000000000000000)

        self.horizontalLayout_2.addWidget(self.trim_gamma)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.trim_time_start = QDoubleSpinBox(self.groupBox)
        self.trim_time_start.setObjectName(u"trim_time_start")
        self.trim_time_start.setFont(font1)
        self.trim_time_start.setCursor(QCursor(Qt.IBeamCursor))
        self.trim_time_start.setMaximum(10000.000000000000000)
        self.trim_time_start.setSingleStep(20.000000000000000)
        self.trim_time_start.setValue(0.000000000000000)

        self.horizontalLayout_3.addWidget(self.trim_time_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.add_trim_btn = QPushButton(self.groupBox)
        self.add_trim_btn.setObjectName(u"add_trim_btn")
        font4 = QFont()
        font4.setFamilies([u"ISOCP_IV50"])
        font4.setPointSize(12)
        self.add_trim_btn.setFont(font4)
        self.add_trim_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.add_trim_btn)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.del_prev_trim_btn = QPushButton(self.groupBox)
        self.del_prev_trim_btn.setObjectName(u"del_prev_trim_btn")
        self.del_prev_trim_btn.setFont(font4)
        self.del_prev_trim_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.del_prev_trim_btn)

        self.clear_trims_btn = QPushButton(self.groupBox)
        self.clear_trims_btn.setObjectName(u"clear_trims_btn")
        self.clear_trims_btn.setFont(font4)
        self.clear_trims_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.clear_trims_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 45))
        font5 = QFont()
        font5.setFamilies([u"ISOCP_IV50"])
        font5.setPointSize(30)
        font5.setBold(False)
        self.label_9.setFont(font5)
        self.label_9.setLineWidth(1)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9.setIndent(-1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.graph_output = QWidget(self.widget)
        self.graph_output.setObjectName(u"graph_output")
        self.graph_output.setMinimumSize(QSize(400, 0))

        self.verticalLayout_5.addWidget(self.graph_output)

        self.graph_selector = QComboBox(self.widget)
        self.graph_selector.setObjectName(u"graph_selector")
        self.graph_selector.setFont(font4)
        self.graph_selector.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.graph_selector)

        self.update_plot_btn = QPushButton(self.widget)
        self.update_plot_btn.setObjectName(u"update_plot_btn")
        self.update_plot_btn.setFont(font4)
        self.update_plot_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.update_plot_btn)

        self.exit_btn = QPushButton(self.widget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setFont(font4)
        self.exit_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.exit_btn)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimuPlane\u2122 0.1.0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Initial Conditions", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocity (m/s)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Flight Path Angle (\u00b0)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity (\u00b0/s)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Altitude (m)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Simulation Time (s)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.run_simulation_btn.setText(QCoreApplication.translate("MainWindow", u"Run Simulation", None))
#if QT_CONFIG(shortcut)
        self.run_simulation_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Velocity (m/s)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Flight Path Angle (\u00b0)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Starting Time (s)", None))
        self.add_trim_btn.setText(QCoreApplication.translate("MainWindow", u"Add Trim", None))
#if QT_CONFIG(shortcut)
        self.add_trim_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.del_prev_trim_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Prev", None))
#if QT_CONFIG(shortcut)
        self.del_prev_trim_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.clear_trims_btn.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
#if QT_CONFIG(shortcut)
        self.clear_trims_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.update_plot_btn.setText(QCoreApplication.translate("MainWindow", u"Update Plot", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Back to Menu", None))
    # retranslateUi

