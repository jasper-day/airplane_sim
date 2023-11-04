from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        self.central_widget = QWidget()  # Create a central widget for the main window
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.stack_widget = QStackedWidget()
        self.layout.addWidget(self.stack_widget)


        self.init_widgets()

    def init_widgets(self):
        # Create multiple widgets to be added to the stack widget
        widget1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel("Widget 1")
        layout1.addWidget(label1)
        widget1.setLayout(layout1)

        widget2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel("Widget 2")
        layout2.addWidget(label2)
        widget2.setLayout(layout2)

        # Add the widgets to the stack widget
        self.stack_widget.addWidget(widget1)
        self.stack_widget.addWidget(widget2)

        # Show the main window with the stacked widgets
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    app.exec()
