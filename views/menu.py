from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont

from db.querys import Query

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = uic.loadUi('views/menu.ui')
        self.menu.show()
        self.menu.btnImoto.clicked.connect(self.insertMoto)
        self.menu.btnInsert.clicked.connect(self.insertRepuesto)
        self.category = []
        self.moto = []
        self.showTable()
        self.showTableRepuestos()
        self.showCategory()
        self.showMoto()
        
        
        
    def showTable(self):
        columns = ['NO.', 'MOTO', 'DESCRIPCION', 'MODELO']
        self.menu.tMoto.setFont(QFont("FiraCode Nerd Font", 12))
        self.menu.tMoto.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.menu.tMoto.setHorizontalHeaderItem(column, QTableWidgetItem(name))
    
    def showTableRepuestos(self):
        columns = ['CÓDIGO', 'DESCRIPCION', 'CATEGORIA', 'MOTO']
        self.menu.tRepuestos.setFont(QFont("FiraCode Nerd Font", 12))
        self.menu.tRepuestos.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.menu.tRepuestos.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        self.menu.tRepuestos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header_style = """
        QHeaderView::section {
            font-family: "FiraCode Nerd Font";
            font-size: 12pt;
            font-weight: bold;
            background-color: rgb(255, 255, 255);
        }
        QTableWidget{
            background-color: rgb(255, 255, 255);
        }
        """
        self.menu.tRepuestos.setStyleSheet(header_style)

    
    def showCategory(self):
        query = Query()
        options = set(self.category)
        result = query.selectCategory()
        for data, datos in enumerate(result):
            options.add(str(datos[1]))
        self.menu.cbCategoria.addItems(list(options))
        
    def showMoto(self):
        query = Query()
        result = query.selectMoto()
        options = set(self.moto)
        for data, datos in enumerate(result):
            options.add(str(datos[1]))
        self.menu.cbMoto.addItems(list(options))
            
            
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
            
    def insertRepuesto(self):
        idcategory = self.menu.cbCategoria.currentIndex()+1
        idmoto = self.menu.cbMoto.currentIndex()+1
        row = self.menu.tRepuestos.rowCount()
        self.menu.tRepuestos.insertRow(row)
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(self.menu.txtCodigo.text()))
        self.menu.tRepuestos.setItem(row, 1, QTableWidgetItem(self.menu.txtDescription.toPlainText()))
        self.menu.tRepuestos.setItem(row, 2, QTableWidgetItem(self.menu.cbCategoria.currentText()))
        self.menu.tRepuestos.setItem(row, 3, QTableWidgetItem(self.menu.cbMoto.currentText()))
        print(idmoto)