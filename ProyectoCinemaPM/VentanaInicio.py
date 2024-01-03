from PyQt6 import QtCore, QtGui, QtWidgets


class VentanaInicio(QtWidgets.QDialog):
    
    def setupVentanaInicio(self, VentanaInicio):

        #se crea la ventana
        VentanaInicio.resize(500, 550)
        VentanaInicio.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaInicio.setWindowTitle("Inicio")

        #Titulo CinemaPm
        self.lblCinemaPm = QtWidgets.QLabel(parent=VentanaInicio)
        self.lblCinemaPm.setGeometry(QtCore.QRect(8, 50, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lblCinemaPm.setFont(font)
        self.lblCinemaPm.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblCinemaPm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCinemaPm.setText("<html><head/><body><p><span style=\" font-style:italic;\">CINEMA</span><span style=\" font-weight:700;\">PM</span></p></body></html>")
        
        #boton vender
        self.btnVender = QtWidgets.QPushButton(parent=VentanaInicio)
        self.btnVender.setGeometry(QtCore.QRect(180, 210, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.btnVender.setFont(font)
        self.btnVender.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius: 20px")
        self.btnVender.clicked.connect(self.abrir_ventana_salas)
        self.btnVender.setText("Vender Entradas")

        #boton resumen
        self.btnResumen = QtWidgets.QPushButton(parent=VentanaInicio)
        self.btnResumen.setGeometry(QtCore.QRect(180, 280, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnResumen.setFont(font)
        self.btnResumen.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius: 20px")
        self.btnResumen.setText("Resumen de ventas")
        self.btnResumen.clicked.connect(self.abrir_ventana_resumenVentas)

        #boton salir
        self.btnSalir = QtWidgets.QPushButton(parent=VentanaInicio)
        self.btnSalir.setGeometry(QtCore.QRect(200, 470, 111, 41))
        self.btnSalir.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius: 20px")
        self.btnSalir.clicked.connect(self.salir)
        self.btnSalir.setText("Salir")
    
    #funcion para salir
    def salir(self):
        
        sys.exit()

    #funcion que abre la ventana de salas al presionar el boton 'Vender entradas'
    def abrir_ventana_salas(self):

        from VentanaSalas import VentanaSalas   #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_salas = VentanaSalas()
        self.ventana_salas.setupSalas(self.ventana_salas)
        self.ventana_salas.show()

    #funcion que abre la ventana de resumen de ventas al presionar el boton 'Resumen de Ventas'
    def abrir_ventana_resumenVentas(self):

        from VentanaResumenVentas import VentanaResumenVentas   #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_resumenVentas = VentanaResumenVentas()
        self.ventana_resumenVentas.setupResumenVentas(self.ventana_resumenVentas)
        self.ventana_resumenVentas.show()

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeInicio = VentanaInicio()
    ui = VentanaInicio()
    ui.setupVentanaInicio(VentanaDeInicio)
    VentanaDeInicio.show()
    sys.exit(app.exec())

