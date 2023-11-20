# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rf_mw.ui'
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
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(906, 753)
        icon = QIcon()
        icon.addFile(u"../source/appicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(64, 64))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"ISOCP_IV50"])
        font.setPointSize(22)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graph_output = QWidget(self.groupBox)
        self.graph_output.setObjectName(u"graph_output")
        self.graph_output.setMinimumSize(QSize(550, 0))

        self.verticalLayout.addWidget(self.graph_output)

        self.graph_selector = QComboBox(self.groupBox)
        self.graph_selector.setObjectName(u"graph_selector")
        font1 = QFont()
        font1.setFamilies([u"ISOCP_IV50"])
        font1.setPointSize(12)
        self.graph_selector.setFont(font1)

        self.verticalLayout.addWidget(self.graph_selector)

        self.elapsed_time = QLineEdit(self.groupBox)
        self.elapsed_time.setObjectName(u"elapsed_time")
        self.elapsed_time.setFont(font1)
        self.elapsed_time.setReadOnly(True)

        self.verticalLayout.addWidget(self.elapsed_time)


        self.horizontalLayout.addWidget(self.groupBox)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(500, 150))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(11)
        self.textBrowser.setFont(font2)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMaximumSize(QSize(500, 16777215))
        font3 = QFont()
        font3.setFamilies([u"ISOCP_IV50"])
        font3.setPointSize(16)
        self.groupBox_3.setFont(font3)
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 9)
        self.widget_4 = QWidget(self.groupBox_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMaximumSize(QSize(16777215, 70))
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.method_selector = QComboBox(self.widget_4)
        self.method_selector.setObjectName(u"method_selector")
        sizePolicy3.setHeightForWidth(self.method_selector.sizePolicy().hasHeightForWidth())
        self.method_selector.setSizePolicy(sizePolicy3)
        self.method_selector.setMaximumSize(QSize(16777215, 70))
        self.method_selector.setFont(font1)

        self.horizontalLayout_5.addWidget(self.method_selector)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(16777215, 70))
        self.label_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.err_selector = QComboBox(self.widget_2)
        self.err_selector.setObjectName(u"err_selector")
        sizePolicy3.setHeightForWidth(self.err_selector.sizePolicy().hasHeightForWidth())
        self.err_selector.setSizePolicy(sizePolicy3)
        self.err_selector.setMaximumSize(QSize(16777215, 70))
        self.err_selector.setFont(font1)

        self.horizontalLayout_4.addWidget(self.err_selector)

        self.err_amt = QLineEdit(self.widget_2)
        self.err_amt.setObjectName(u"err_amt")
        sizePolicy3.setHeightForWidth(self.err_amt.sizePolicy().hasHeightForWidth())
        self.err_amt.setSizePolicy(sizePolicy3)
        self.err_amt.setMinimumSize(QSize(0, 0))
        self.err_amt.setMaximumSize(QSize(150, 70))
        self.err_amt.setFont(font1)

        self.horizontalLayout_4.addWidget(self.err_amt)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setMaximumSize(QSize(500, 16777215))
        self.groupBox_2.setFont(font3)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        self.label_3.setMaximumSize(QSize(16777215, 70))
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.gamma_max = QDoubleSpinBox(self.groupBox_2)
        self.gamma_max.setObjectName(u"gamma_max")
        sizePolicy5.setHeightForWidth(self.gamma_max.sizePolicy().hasHeightForWidth())
        self.gamma_max.setSizePolicy(sizePolicy5)
        self.gamma_max.setMaximumSize(QSize(16777215, 70))
        self.gamma_max.setFont(font1)
        self.gamma_max.setMaximum(50.000000000000000)
        self.gamma_max.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.gamma_max, 1, 2, 1, 1)

        self.vel_min = QDoubleSpinBox(self.groupBox_2)
        self.vel_min.setObjectName(u"vel_min")
        sizePolicy5.setHeightForWidth(self.vel_min.sizePolicy().hasHeightForWidth())
        self.vel_min.setSizePolicy(sizePolicy5)
        self.vel_min.setMaximumSize(QSize(16777215, 70))
        self.vel_min.setFont(font1)
        self.vel_min.setMinimum(-100.000000000000000)
        self.vel_min.setMaximum(1000.000000000000000)
        self.vel_min.setSingleStep(10.000000000000000)
        self.vel_min.setValue(30.000000000000000)

        self.gridLayout_2.addWidget(self.vel_min, 2, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.vel_max = QDoubleSpinBox(self.groupBox_2)
        self.vel_max.setObjectName(u"vel_max")
        sizePolicy5.setHeightForWidth(self.vel_max.sizePolicy().hasHeightForWidth())
        self.vel_max.setSizePolicy(sizePolicy5)
        self.vel_max.setMaximumSize(QSize(16777215, 70))
        self.vel_max.setFont(font1)
        self.vel_max.setMinimum(-100.000000000000000)
        self.vel_max.setMaximum(1000.000000000000000)
        self.vel_max.setSingleStep(10.000000000000000)
        self.vel_max.setValue(400.000000000000000)

        self.gridLayout_2.addWidget(self.vel_max, 3, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setMaximumSize(QSize(16777215, 70))
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.gamma_min = QDoubleSpinBox(self.groupBox_2)
        self.gamma_min.setObjectName(u"gamma_min")
        sizePolicy5.setHeightForWidth(self.gamma_min.sizePolicy().hasHeightForWidth())
        self.gamma_min.setSizePolicy(sizePolicy5)
        self.gamma_min.setMaximumSize(QSize(16777215, 70))
        self.gamma_min.setFont(font1)
        self.gamma_min.setMinimum(-50.000000000000000)
        self.gamma_min.setMaximum(0.000000000000000)
        self.gamma_min.setValue(-30.000000000000000)

        self.gridLayout_2.addWidget(self.gamma_min, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(16777215, 70))
        self.horizontalSlider.setFont(font1)
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
        self.fix_vel.setMaximumSize(QSize(16777215, 70))
        self.fix_vel.setFont(font1)
        self.fix_vel.setChecked(False)

        self.gridLayout.addWidget(self.fix_vel, 0, 0, 1, 1)

        self.fix_gamma = QRadioButton(self.groupBox_2)
        self.fix_gamma.setObjectName(u"fix_gamma")
        self.fix_gamma.setMaximumSize(QSize(16777215, 70))
        self.fix_gamma.setFont(font1)
        self.fix_gamma.setChecked(True)

        self.gridLayout.addWidget(self.fix_gamma, 1, 0, 1, 1)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 70))
        self.widget.setFont(font1)
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
        sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
        self.return_btn.setSizePolicy(sizePolicy)
        self.return_btn.setMinimumSize(QSize(0, 30))
        self.return_btn.setMaximumSize(QSize(500, 16777215))
        self.return_btn.setFont(font1)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimuPlane\u2122 1.0.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI Light'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">This section generates plots of trim conditions at different velocities and pitch angles.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">To use it, simply select which option to fix, then drag the slider.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">You can also play with the maximum and minimum values for velocity and pitch angle.</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Simulation Options", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Root Finding Method:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Convergence criteria:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum Velocity (m/s)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Minimum Flight Path Angle (deg)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Maximum Flight Path Angle (deg)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Maximum Velocity (m/s)", None))
        self.fix_vel.setText(QCoreApplication.translate("MainWindow", u"Select Velocity", None))
        self.fix_gamma.setText(QCoreApplication.translate("MainWindow", u"Select Flight Path Angle", None))
        self.slider_label.setText(QCoreApplication.translate("MainWindow", u"Velocity:", None))
        self.return_btn.setText(QCoreApplication.translate("MainWindow", u"Back to Menu", None))
#if QT_CONFIG(shortcut)
        self.return_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

