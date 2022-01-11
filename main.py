from calculator import App
import sys
from PyQt5.QtWidgets import QApplication

q_app = QApplication(sys.argv)
app = App()

app.show()
q_app.exec_()


