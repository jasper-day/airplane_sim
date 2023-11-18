# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rf_mw.ui'
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
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graph_output = QWidget(self.groupBox)
        self.graph_output.setObjectName(u"graph_output")

        self.verticalLayout.addWidget(self.graph_output)

        self.graph_selector = QComboBox(self.groupBox)
        self.graph_selector.setObjectName(u"graph_selector")

        self.verticalLayout.addWidget(self.graph_selector)

        self.elapsed_time = QLineEdit(self.groupBox)
        self.elapsed_time.setObjectName(u"elapsed_time")
        self.elapsed_time.setReadOnly(True)

        self.verticalLayout.addWidget(self.elapsed_time)


        self.horizontalLayout.addWidget(self.groupBox)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.method_selector = QComboBox(self.groupBox_2)
        self.method_selector.setObjectName(u"method_selector")

        self.verticalLayout_3.addWidget(self.method_selector)

        self.widget_2 = QWidget(self.groupBox_2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.err_selector = QComboBox(self.widget_2)
        self.err_selector.setObjectName(u"err_selector")

        self.horizontalLayout_4.addWidget(self.err_selector)

        self.err_amt = QLineEdit(self.widget_2)
        self.err_amt.setObjectName(u"err_amt")

        self.horizontalLayout_4.addWidget(self.err_amt)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.gamma_max = QDoubleSpinBox(self.groupBox_2)
        self.gamma_max.setObjectName(u"gamma_max")
        self.gamma_max.setMaximum(50.000000000000000)
        self.gamma_max.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.gamma_max, 1, 2, 1, 1)

        self.vel_min = QDoubleSpinBox(self.groupBox_2)
        self.vel_min.setObjectName(u"vel_min")
        self.vel_min.setMinimum(-100.000000000000000)
        self.vel_min.setMaximum(1000.000000000000000)
        self.vel_min.setSingleStep(10.000000000000000)
        self.vel_min.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.vel_min, 2, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.vel_max = QDoubleSpinBox(self.groupBox_2)
        self.vel_max.setObjectName(u"vel_max")
        self.vel_max.setMinimum(-100.000000000000000)
        self.vel_max.setMaximum(1000.000000000000000)
        self.vel_max.setSingleStep(10.000000000000000)
        self.vel_max.setValue(400.000000000000000)

        self.gridLayout_2.addWidget(self.vel_max, 3, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.gamma_min = QDoubleSpinBox(self.groupBox_2)
        self.gamma_min.setObjectName(u"gamma_min")
        self.gamma_min.setMinimum(-50.000000000000000)
        self.gamma_min.setMaximum(0.000000000000000)
        self.gamma_min.setValue(-30.000000000000000)

        self.gridLayout_2.addWidget(self.gamma_min, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(30)
        self.horizontalSlider.setMaximum(400)
        self.horizontalSlider.setValue(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)

        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 1)

        self.fix_vel = QRadioButton(self.groupBox_2)
        self.fix_vel.setObjectName(u"fix_vel")
        self.fix_vel.setChecked(False)

        self.gridLayout.addWidget(self.fix_vel, 0, 0, 1, 1)

        self.fix_gamma = QRadioButton(self.groupBox_2)
        self.fix_gamma.setObjectName(u"fix_gamma")
        self.fix_gamma.setChecked(True)

        self.gridLayout.addWidget(self.fix_gamma, 1, 0, 1, 1)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_label = QLabel(self.widget)
        self.slider_label.setObjectName(u"slider_label")

        self.horizontalLayout_3.addWidget(self.slider_label)

        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 100.000000000000000)

        self.horizontalLayout_3.addWidget(self.lcdNumber)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.return_btn = QPushButton(self.widget_3)
        self.return_btn.setObjectName(u"return_btn")

        self.verticalLayout_2.addWidget(self.return_btn)


        self.horizontalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.vel_min)
        self.label.setBuddy(self.gamma_min)
        self.label_2.setBuddy(self.gamma_max)
        self.label_4.setBuddy(self.vel_max)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.gamma_min, self.gamma_max)
        QWidget.setTabOrder(self.gamma_max, self.vel_min)
        QWidget.setTabOrder(self.vel_min, self.vel_max)
        QWidget.setTabOrder(self.vel_max, self.fix_vel)
        QWidget.setTabOrder(self.fix_vel, self.fix_gamma)
        QWidget.setTabOrder(self.fix_gamma, self.textBrowser)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This section generates plots of trim conditions at different velocities and pitch angles.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To use it, simply select"
                        " which option to fix, then drag the slider.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can also play with the maximum and minimum values for velocity and pitch angle.</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum Velocity (m/s)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Minimum Flight Path Angle (deg)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Maximum Flight Path Angle (deg)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Maximum Velocity (m/s)", None))
        self.fix_vel.setText(QCoreApplication.translate("MainWindow", u"Select Velocity", None))
        self.fix_gamma.setText(QCoreApplication.translate("MainWindow", u"Select Flight Path Angle", None))
        self.slider_label.setText(QCoreApplication.translate("MainWindow", u"Velocity:", None))
        self.return_btn.setText(QCoreApplication.translate("MainWindow", u"Back to Menu", None))
    # retranslateUi

