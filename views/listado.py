from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont
from db.querys import Query

class Catalogos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.catalogo = uic.loadUi('views/catalogo.ui')
        self.catalogo.show()
        self.catalogo.btnSearch.clicked.connect(self.clearTable)
        self.catalogo.cbMotoL.currentIndexChanged.connect(self.searchRepuestoMoto)
        self.catalogo.cbCategoryL.currentIndexChanged.connect(self.searchRepuestoCategory)
        self.showClistado()
        self.showMoto()
        
        
    def showClistado(self):
        query = Query()
        result = query.selectCategory()
        for id, data in result:
            self.catalogo.cbCategoryL.addItem(str(data))
        
    
    def showMoto(self):
        query = Query()
        result = query.selectMotoSearch()
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
        
    def showTableMotos(self):
        columns = ['CÓDIGO', 'DESCRIPCION', 'CATEGORIA','NOMBRE']
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
        self.showTableRepuestos()
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
        self.showTableMotos()
        query = Query()
        self.nombre = self.catalogo.cbMotoL.currentText()
        print(self.nombre)
        result = query.selectRepuestosMotos(self.nombre)
        for row in result:
            cod = row[0]
            description = row[1]
            category = row[2]
            moto = row[3]
            row_index = self.catalogo.tRepuestosL.rowCount()
            self.catalogo.tRepuestosL.insertRow(row_index)
            self.catalogo.tRepuestosL.setItem(row_index, 0, QTableWidgetItem(str(cod)))
            self.catalogo.tRepuestosL.setItem(row_index, 1, QTableWidgetItem(str(description)))
            self.catalogo.tRepuestosL.setItem(row_index, 2, QTableWidgetItem(str(category)))
            self.catalogo.tRepuestosL.setItem(row_index, 3, QTableWidgetItem(str(moto)))
        self.catalogo.cbMotoL.setCurrentIndex(-1)
        print(result)
        
    def searchRepuestoCategory(self):
        self.category = self.catalogo.cbCategoryL.currentText()
        for row in range(self.catalogo.tRepuestosL.rowCount()):
            row_text=[self.catalogo.tRepuestosL.item(row, col).text().upper() for col in range(self.catalogo.tRepuestosL.columnCount())]
            print(row_text)
            if any(self.category in text for text in row_text):
                self.catalogo.tRepuestosL.setRowHidden(row, False)
            else:
                self.catalogo.tRepuestosL.setRowHidden(row,True)
        self.catalogo.cbCategoryL.setCurrentIndex(-1)
                  
    def clearTable(self):
        self.catalogo.tRepuestosL.setRowCount(0)