from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

from db.querys import Query

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = uic.loadUi('views/menu.ui')
        self.menu.show()
        self.menu.btnImoto.clicked.connect(self.insertMoto)
        self.showTable()
        
        
        
    def showTable(self):
        columns = ['NO.', 'MOTO', 'DESCRIPCION', 'MODELO']
        self.menu.tMoto.setFont(QFont("FiraCode Nerd Font", 14))
        self.menu.tMoto.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.menu.tMoto.setHorizontalHeaderItem(column, QTableWidgetItem(name))
            
    def insertMoto(self):
        self.descripcion = self.menu.txtDmoto.toPlainText().strip()
        self.nombre = self.menu.txtName.text()
        self.modelo = int(self.menu.cbYear.currentText())
        query = Query()
        if self.descripcion:
            query.insertMoto(self.nombre, self.descripcion, self.modelo)
        else: 
            self.descripcion = ''
            query.insertMoto(self.nombre, self.descripcion, self.modelo)