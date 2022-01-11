from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLineEdit

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        btn = QPushButton('Test')

        grid = QGridLayout()

        grid.addWidget(btn)

        widget = QWidget()

        widget.setLayout(grid)

        self.setCentralWidget(widget)

