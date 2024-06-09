from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

from .menu import Menu

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi('views/home.ui')
        self.main.show()
        self.main.btnRepuestos.clicked.connect(self.showInsertRepuestos)
        
    def showInsertRepuestos(self):
        self.menu = Menu()
        self.main.close()