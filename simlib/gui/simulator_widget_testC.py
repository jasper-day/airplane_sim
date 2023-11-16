# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulator_widget_test.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import resourcefile_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1066, 776)
        self.horizontalLayout_11 = QHBoxLayout(Form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.GraphOutput = QFrame(self.widget)
        self.GraphOutput.setObjectName(u"GraphOutput")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.GraphOutput.sizePolicy().hasHeightForWidth())
        self.GraphOutput.setSizePolicy(sizePolicy)
        self.GraphOutput.setFrameShape(QFrame.StyledPanel)
        self.GraphOutput.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.GraphOutput)

        self.graph_selector = QComboBox(self.widget)
        self.graph_selector.setObjectName(u"graph_selector")

        self.verticalLayout_5.addWidget(self.graph_selector)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_11.addWidget(self.widget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.trim_input_table = QTableView(Form)
        self.trim_input_table.setObjectName(u"trim_input_table")

        self.verticalLayout_3.addWidget(self.trim_input_table)

        self.trim_output_table = QTableView(Form)
        self.trim_output_table.setObjectName(u"trim_output_table")

        self.verticalLayout_3.addWidget(self.trim_output_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_3 = QGroupBox(Form)
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

        self.init_altitude = QLineEdit(self.groupBox_3)
        self.init_altitude.setObjectName(u"init_altitude")

        self.horizontalLayout_7.addWidget(self.init_altitude)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.init_ttime = QLineEdit(self.groupBox_3)
        self.init_ttime.setObjectName(u"init_ttime")

        self.horizontalLayout_8.addWidget(self.init_ttime)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(Form)
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

        self.trim_tstart = QLineEdit(self.groupBox)
        self.trim_tstart.setObjectName(u"trim_tstart")

        self.horizontalLayout_3.addWidget(self.trim_tstart)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.add_trim = QPushButton(self.groupBox)
        self.add_trim.setObjectName(u"add_trim")

        self.verticalLayout.addWidget(self.add_trim)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.del_prev_trim = QPushButton(self.groupBox)
        self.del_prev_trim.setObjectName(u"del_prev_trim")

        self.horizontalLayout_9.addWidget(self.del_prev_trim)

        self.clear_trims = QPushButton(self.groupBox)
        self.clear_trims.setObjectName(u"clear_trims")

        self.horizontalLayout_9.addWidget(self.clear_trims)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.run_simulation = QPushButton(Form)
        self.run_simulation.setObjectName(u"run_simulation")

        self.verticalLayout_4.addWidget(self.run_simulation)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.Movielabel = QLabel(Form)
        self.Movielabel.setObjectName(u"Movielabel")
        self.Movielabel.setPixmap(QPixmap(u":/gif/P51.gif"))
        self.Movielabel.setScaledContents(False)

        self.horizontalLayout_11.addWidget(self.Movielabel)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_11.addLayout(self.verticalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Output", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Back to Menu", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Initial Conditions", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Velocity (m/s)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Flight Path Angle (\u00b0)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Angular Velocity (\u00b0/s)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Altitude (m)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Simulation time (s)", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Commands", None))
        self.label.setText(QCoreApplication.translate("Form", u"Velocity (m/s)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Flight Path Angle (\u00b0)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Starting Time (s)", None))
        self.add_trim.setText(QCoreApplication.translate("Form", u"Add Trim", None))
        self.del_prev_trim.setText(QCoreApplication.translate("Form", u"Delete Prev", None))
        self.clear_trims.setText(QCoreApplication.translate("Form", u"Clear All", None))
        self.run_simulation.setText(QCoreApplication.translate("Form", u"Run Simulation", None))
    # retranslateUi

