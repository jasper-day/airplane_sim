import sys
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QPushButton,
)


class Widget1(QWidget):
    def __init__(self, parent=None):
        super(Widget1, self).__init__(parent)
        self.resize(1200,800)
        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")

        self.button = QPushButton("Start", self)
        # self.button.clicked.connect(self.switch_widget)
        self.button1 = QPushButton("Quit",self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addWidget(self.button1, 2, 0)

        self.setLayout(self.layout)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout Example")
        # Create a top-level layout
        layout = QVBoxLayout(self)
        # Create and connect the combo box to switch between pages
        # self.pageCombo = QComboBox()
        # self.pageCombo.addItems(["Page 1", "Page 2"])
        # self.pageCombo.activated.connect(self.switchPage)
        
        self.label = QtWidgets.QLabel(self)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("p51_3d.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("QLabel {background-color: white;}")
        
        self.button1 = QPushButton("Start", self)
        self.button1.clicked.connect(self.switchtoPage1)
        self.button2 = QPushButton("Home",self)
        self.button2.clicked.connect(self.switchtoPage0)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)
        
        # Create the stacked layout
        self.stackedLayout = QStackedLayout()
        
        
        
        # Create the first page
        self.page1 = QWidget()
        self.page1Layout = QFormLayout()
        self.page1Layout.addRow("Name:", QLineEdit())
        self.page1Layout.addRow("Address:", QLineEdit())
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        
        
        
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QFormLayout()
        self.page2Layout.addRow("Job:", QLineEdit())
        self.page2Layout.addRow("Department:", QLineEdit())
        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        # Add the combo box and the stacked layout to the top-level layout
        # layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)

    def switchtoPage0(self):
        self.stackedLayout.setCurrentIndex(0)

    def switchtoPage1(self):
        self.stackedLayout.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())