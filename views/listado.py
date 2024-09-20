from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont
from db.querys import Query

class Catalogos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.catalogo = uic.loadUi('views/catalogo.ui')
        self.catalogo.show()
        self.catalogo.btnSearch.clicked.connect(self.searchRepuestos)
        self.catalogo.cbMotoL.currentIndexChanged.connect(self.searchRepuestoMoto)
        self.showClistado()
        self.showMoto()
        self.showTableRepuestos()
        
    def showClistado(self):
        query = Query()
        result = query.selectCategory()
        for id, data in result:
            self.catalogo.cbCategoryL.addItem(str(data))
        
    
    def showMoto(self):
        query = Query()
        result = query.selectMoto()
        for id, data in result:
            self.catalogo.cbMotoL.addItem(str(data))
            
    def showTableRepuestos(self):
        columns = ['CÓDIGO', 'DESCRIPCION']
        self.catalogo.tRepuestosL.setFont(QFont("FiraCode Nerd Font", 12))
        self.catalogo.tRepuestosL.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.catalogo.tRepuestosL.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        self.catalogo.tRepuestosL.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
        self.catalogo.tRepuestosL.setStyleSheet(header_style)
        
    def searchRepuestos(self):
        query = Query()
        self.codigo = self.catalogo.txtCodeName.text()
        cod = str(self.codigo)
        result = query.selectRepuestos(cod.upper())
        row_index = self.catalogo.tRepuestosL.rowCount()
        self.catalogo.tRepuestosL.insertRow(row_index)
        self.catalogo.tRepuestosL.setItem(row_index, 0, QTableWidgetItem(str(result[0][0])))
        self.catalogo.tRepuestosL.setItem(row_index, 1, QTableWidgetItem(str(result[0][1])))
        print(result)
        
    def searchRepuestoMoto(self):
        query = Query()
        nombre = str(self.catalogo.cbMotoL.currentText()).split()

        print(nombre[0])