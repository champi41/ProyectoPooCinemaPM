from PyQt6 import QtCore, QtGui, QtWidgets


class VentanaResumenVentas(QtWidgets.QDialog):
    
    def setupResumenVentas(self, VentanaResumenVentas):
        
        #se crea la ventana
        VentanaResumenVentas.resize(500, 550)
        VentanaResumenVentas.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaResumenVentas.setWindowTitle("Rseumen de Ventas")
        
        #texto resumen de ventas
        self.lblResumenVentas = QtWidgets.QLabel(parent=VentanaResumenVentas)
        self.lblResumenVentas.setGeometry(QtCore.QRect(0, 10, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblResumenVentas.setFont(font)
        self.lblResumenVentas.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblResumenVentas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResumenVentas.setText("Resumen de ventas")

        #se crea la tabla 
        self.tableWResumen = QtWidgets.QTableWidget(parent=VentanaResumenVentas)
        self.tableWResumen.setGeometry(QtCore.QRect(12, 100, 470, 361))
        self.tableWResumen.setStyleSheet("background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.tableWResumen.setShowGrid(True)
        self.tableWResumen.setColumnCount(4)
        self.tableWResumen.setRowCount(7)

        #se generan las filas para la informacion, en este caso creamos 7 espacios
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setVerticalHeaderItem(6, item)

        #se crean las columnas, sala, horario, asientos y total
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWResumen.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWResumen.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWResumen.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWResumen.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWResumen.setItem(0, 3, item)
        self.tableWResumen.horizontalHeader().setDefaultSectionSize(113)

        item = self.tableWResumen.verticalHeaderItem(0)
        item.setText("1")
        item = self.tableWResumen.verticalHeaderItem(1)
        item.setText("2")
        item = self.tableWResumen.verticalHeaderItem(2)
        item.setText("3")
        item = self.tableWResumen.verticalHeaderItem(3)
        item.setText("4")
        item = self.tableWResumen.verticalHeaderItem(4)
        item.setText("5")
        item = self.tableWResumen.verticalHeaderItem(5)
        item.setText("6")
        item = self.tableWResumen.verticalHeaderItem(6)
        item.setText("7")
        item = self.tableWResumen.horizontalHeaderItem(0)
        item.setText("Sala")
        item = self.tableWResumen.horizontalHeaderItem(1)
        item.setText("Horario")
        item = self.tableWResumen.horizontalHeaderItem(2)
        item.setText("Asientos")
        item = self.tableWResumen.horizontalHeaderItem(3)
        item.setText("Total")
        
        __sortingEnabled = self.tableWResumen.isSortingEnabled()
        self.tableWResumen.setSortingEnabled(False)

        #aqui se muestran los datos que contiene el arreglo
        from VentanaAsientos import textoS1_3pm, textoS1_6pm, textoS1_9pm

        if len(textoS1_3pm) > 2:
            
                total1 = 3000*len(textoS1_3pm[2:])
                item = self.tableWResumen.item(0, 0)
                item.setText(str(textoS1_3pm[0]))
                item = self.tableWResumen.item(0, 1)
                item.setText(str(textoS1_3pm[1]))
                item = self.tableWResumen.item(0, 2)
                item.setText(str(textoS1_3pm[2:]))
                item = self.tableWResumen.item(0, 3)
                item.setText(str(total1))
                self.tableWResumen.setSortingEnabled(__sortingEnabled)

        elif len(textoS1_6pm) > 2:
             
                total2 = 3000*len(textoS1_6pm[2:])
                item = self.tableWResumen.item(0, 0)
                item.setText(str(textoS1_6pm[0]))
                item = self.tableWResumen.item(0, 1)
                item.setText(str(textoS1_6pm[1]))
                item = self.tableWResumen.item(0, 2)
                item.setText(str(textoS1_6pm[2:]))
                item = self.tableWResumen.item(0, 3)
                item.setText(str(total2))
                self.tableWResumen.setSortingEnabled(__sortingEnabled)

        elif len(textoS1_9pm) > 2:
             
                total3 = 3000*len(textoS1_9pm[2:])
                item = self.tableWResumen.item(0, 0)
                item.setText(str(textoS1_9pm[0]))
                item = self.tableWResumen.item(0, 1)
                item.setText(str(textoS1_9pm[1]))
                item = self.tableWResumen.item(0, 2)
                item.setText(str(textoS1_9pm[2:]))
                item = self.tableWResumen.item(0, 3)
                item.setText(str(total3))
                self.tableWResumen.setSortingEnabled(__sortingEnabled)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeResumenVentas = QtWidgets.QDialog()
    ui = VentanaResumenVentas()
    ui.setupResumenVentas(VentanaDeResumenVentas)
    VentanaDeResumenVentas.show()
    sys.exit(app.exec())
