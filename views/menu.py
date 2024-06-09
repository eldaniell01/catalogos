import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont

from db.querys import Query

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = uic.loadUi('views/menu.ui')
        self.menu.show()
        self.menu.btnImoto.clicked.connect(self.insertMoto)
        self.menu.btnInsert.clicked.connect(self.insertRepuesto)
        self.menu.btnImagen.clicked.connect(self.openImagen)
        self.category = []
        self.moto = []
        self.img = []
        self.showTable()
        self.showTableRepuestos()
        self.showCategory()
        self.showMoto()
        
        
        
    def showTable(self):
        columns = ['MOTO', 'DESCRIPCION', 'MODELO', 'MARCA']
        self.menu.tMoto.setFont(QFont("FiraCode Nerd Font", 12))
        self.menu.tMoto.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.menu.tMoto.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        self.menu.tMoto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
        self.menu.tMoto.setStyleSheet(header_style)
    
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
        print(result)
        for id, data in result:
            print(id)
            print(data)
            self.menu.cbMoto.addItem(str(data))
        """for data, datos in enumerate(result):
            print(datos)
            options.add(str(datos[1]))
            
        selects = list(options)
        selects.sort()
        self.menu.cbMoto.addItems(selects)"""
            
    def insertMoto(self):
        self.descripcion = self.menu.txtDmoto.toPlainText().strip()
        self.nombre = self.menu.txtName.text()
        self.modelo = int(self.menu.cbYear.currentText())
        self.marca = self.menu.txtMarca.text()
        query = Query()
        if self.descripcion:
            query.insertMoto(self.nombre, self.descripcion, self.modelo, self.marca)
        else: 
            self.descripcion = ''
            query.insertMoto(self.nombre, self.descripcion, self.modelo, self.marca)
            
        row = self.menu.tMoto.rowCount()
        self.menu.tRepuestos.insertRow(row)
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(self.nombre))
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(self.descripcion))
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(str(self.modelo)))
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(self.marca))
        self.menu.cbMoto.clear()
        self.showMoto()
            
    def insertRepuesto(self):
        query = Query()
        idcategory = self.menu.cbCategoria.currentIndex()+1
        idmoto = self.menu.cbMoto.currentIndex()+1
        for ruta_imagen in self.img:
                if os.path.exists(ruta_imagen):
                    with open(ruta_imagen, 'rb') as file:
                        print(ruta_imagen)
                        imagen_binaria = file.read()
                        query.insertRepuesto(self.menu.txtCodigo.text(), self.menu.txtDescription.toPlainText(), imagen_binaria, idcategory, idmoto)
                else: 
                    print('error')
        
        row = self.menu.tRepuestos.rowCount()
        self.menu.tRepuestos.insertRow(row)
        self.menu.tRepuestos.setItem(row, 0, QTableWidgetItem(self.menu.txtCodigo.text()))
        self.menu.tRepuestos.setItem(row, 1, QTableWidgetItem(self.menu.txtDescription.toPlainText()))
        self.menu.tRepuestos.setItem(row, 2, QTableWidgetItem(self.menu.cbCategoria.currentText()))
        self.menu.tRepuestos.setItem(row, 3, QTableWidgetItem(self.menu.cbMoto.currentText()))
    
    def openImagen(self):
        folder = QFileDialog()
        folder_path, __= folder.getOpenFileNames(None, 'Cargar imagen', '', 'JPEG (*.jpg)')
        self.img = folder_path
        