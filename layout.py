import os
import webbrowser
from PyQt6.QtWidgets import QPushButton, QWidget, QGridLayout
from PyQt6.QtGui import QPainter, QPixmap
class Website(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window")
        self.resize(900, 700)

        self.background = QPixmap(os.path.join(os.path.dirname(__file__), "background.png"))

        layout = QGridLayout()
        self.setLayout(layout)

        button1= QPushButton("Google")
        button1.setFixedSize(160, 60)
        def open_google():
            webbrowser.open('http://www.google.com')
        button1.clicked.connect(open_google)
        layout.addWidget(button1)

        button2= QPushButton("Weather")
        button2.setFixedSize(160, 60)
        def open_weather():
            webbrowser.open('http://www.weather.com')
        button2.clicked.connect(open_weather)
        layout.addWidget(button2)

        button3= QPushButton("Facebook")
        button3.setFixedSize(160, 60)
        def open_facebook():
            webbrowser.open('http://www.facebook.com')
        button3.clicked.connect(open_facebook)
        layout.addWidget(button3)

        button4= QPushButton("YouTube")
        button4.setFixedSize(160, 60)
        def open_youtube():
            webbrowser.open('http://www.youtube.com')
        button4.clicked.connect(open_youtube)
        layout.addWidget(button4)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background)