import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow
from PyQt6.QtGui import QMovie

class ResizableGifWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.gif_label = QLabel(self.central_widget)
        self.gif_movie = QMovie('P51_3d.gif')  # Replace 'your_gif_file.gif' with your GIF file path
        self.gif_label.setMovie(self.gif_movie)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.gif_label)

        self.setWindowTitle('Resizable GIF')
        self.setGeometry(100, 100, 600, 400)  # Set an initial size

        self.show()

    def resizeEvent(self, event):
        self.resizeGif()

    def resizeGif(self):
        current_size = self.gif_label.size()

        new_size = self.central_widget.size()
        new_size.setWidth(new_size.width() - 20)  # Adjust for any margins or padding
        new_size.setHeight(new_size.height() - 20)

        aspect_ratio = current_size.width() / current_size.height()

        if new_size.width() / aspect_ratio > new_size.height():
            new_width = int(new_size.height() * aspect_ratio)
            new_height = new_size.height()
        else:
            new_width = new_size.width()
            new_height = int(new_size.width() / aspect_ratio)

        self.gif_label.setFixedSize(new_width, new_height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResizableGifWidget()
    window.show()
    sys.exit(app.exec())
