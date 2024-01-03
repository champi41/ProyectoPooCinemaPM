from PyQt6 import QtCore, QtGui, QtWidgets


class VentanaHorarios(QtWidgets.QDialog):
    
    def setupHorarios(self, VentanaHorarios):
        
        #se crea la ventana
        VentanaHorarios.resize(500, 550)
        VentanaHorarios.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaHorarios.setWindowTitle("Horarios")

        #titulo seleccione el horario
        self.lblSeleccioneHorario = QtWidgets.QLabel(parent=VentanaHorarios)
        self.lblSeleccioneHorario.setGeometry(QtCore.QRect(0, 20, 500, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblSeleccioneHorario.setFont(font)
        self.lblSeleccioneHorario.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblSeleccioneHorario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSeleccioneHorario.setText("Seleccione el Horario")

        #boton 3 pm
        self.btn3pm = QtWidgets.QPushButton(parent=VentanaHorarios)
        self.btn3pm.setGeometry(QtCore.QRect(170, 190, 160, 40))
        self.btn3pm.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius:20px")
        self.btn3pm.clicked.connect(self.abrir_ventana_asientosS1_3pm)
        self.btn3pm.setText("3 pm")

        #boton 6 pm
        self.btn6pm = QtWidgets.QPushButton(parent=VentanaHorarios)
        self.btn6pm.setGeometry(QtCore.QRect(170, 250, 160, 40))
        self.btn6pm.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius:20px")
        self.btn6pm.clicked.connect(self.abrir_ventana_asientosS1_6pm)
        self.btn6pm.setText("6 pm")

        #boton 9 pm
        self.btn9pm = QtWidgets.QPushButton(parent=VentanaHorarios)
        self.btn9pm.setGeometry(QtCore.QRect(170, 310, 160, 40))
        self.btn9pm.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius:20px")
        self.btn9pm.clicked.connect(self.abrir_ventana_asientosS1_9pm)
        self.btn9pm.setText("9 pm")

    #funcion que abre la ventana de asientos de las 3 pm    
    def abrir_ventana_asientosS1_3pm(self):

        from VentanaAsientos import VentanaAsientosS1_3pm   #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_asientos = VentanaAsientosS1_3pm()
        self.ventana_asientos.setupAsientos(self.ventana_asientos)
        self.ventana_asientos.show()
   
    #funcion que abre la ventana de asientos de las 6 pm
    def abrir_ventana_asientosS1_6pm(self):

        from VentanaAsientos import VentanaAsientosS1_6pm   #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_asientos = VentanaAsientosS1_6pm()
        self.ventana_asientos.setupAsientos(self.ventana_asientos)
        self.ventana_asientos.show()
    
    #funcion que abre la ventana de asientos de las 9 pm
    def abrir_ventana_asientosS1_9pm(self):

        from VentanaAsientos import VentanaAsientosS1_9pm   #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_asientos = VentanaAsientosS1_9pm()
        self.ventana_asientos.setupAsientos(self.ventana_asientos)
        self.ventana_asientos.show()
    
if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeHorarios = QtWidgets.QDialog()
    ui = VentanaHorarios()
    ui.setupHorarios(VentanaDeHorarios)
    VentanaDeHorarios.show()
    sys.exit(app.exec())
