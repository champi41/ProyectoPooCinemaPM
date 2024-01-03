from PyQt6 import QtCore, QtGui, QtWidgets

class VentanaResCom(QtWidgets.QDialog):
    
    def setupResCom(self, VentanaResCom):

        #se crea la ventana
        VentanaResCom.resize(500, 550)
        VentanaResCom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaResCom.setWindowTitle("Resumen de Compra")

        #titulo resumen de compra
        self.lblResumenCompra = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblResumenCompra.setGeometry(QtCore.QRect(0, 30, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblResumenCompra.setFont(font)
        self.lblResumenCompra.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblResumenCompra.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResumenCompra.setText("Resumen de Compra")

        #texto 'sala'
        self.lblSala = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblSala.setGeometry(QtCore.QRect(20, 170, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblSala.setFont(font)
        self.lblSala.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblSala.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblSala.setText("Sala: ")

        #texto 'horario'
        self.lblHorario = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblHorario.setGeometry(QtCore.QRect(20, 230, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblHorario.setFont(font)
        self.lblHorario.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblHorario.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblHorario.setText("Horario:")

        #texto 'asientos'
        self.lblAsientos = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblAsientos.setGeometry(QtCore.QRect(20, 290, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblAsientos.setFont(font)
        self.lblAsientos.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblAsientos.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblAsientos.setText("Asientos:")

        #texto de los datos de la sala
        self.lblDatosSala = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblDatosSala.setGeometry(QtCore.QRect(80, 170, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblDatosSala.setFont(font)
        self.lblDatosSala.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")

        #texto de los datos del horario
        self.lblDatosHorario = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblDatosHorario.setGeometry(QtCore.QRect(110, 230, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblDatosHorario.setFont(font)
        self.lblDatosHorario.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")

        #texto de los datos de los asientos
        self.lblDatosAsientos = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblDatosAsientos.setGeometry(QtCore.QRect(120, 290, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblDatosAsientos.setFont(font)
        self.lblDatosAsientos.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")

        #mensaje de cerrar ventanas (se opto a esto porque no pudimos hacer una funcion para cerrar las ventanas menos la principal)
        self.lblFin = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblFin.setGeometry(QtCore.QRect(180, 420, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblFin.setFont(font)
        self.lblFin.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblFin.setText("Puede cerrar las ventanas")

        #texto 'total'
        self.lblTotal = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblTotal.setGeometry(QtCore.QRect(20, 350, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTotal.setFont(font)
        self.lblTotal.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblTotal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblTotal.setText("Total a pagar: $")

        #texto de los datos del precio final
        self.lblDatosTotal = QtWidgets.QLabel(parent=VentanaResCom)
        self.lblDatosTotal.setGeometry(QtCore.QRect(170, 350, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblDatosTotal.setFont(font)
        self.lblDatosTotal.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")

        from VentanaAsientos import textoS1_3pm, textoS1_6pm, textoS1_9pm

        precioEntrada = 3000
        #se usa len() para contar la cantidad de elementos en el arreglo y asi saber en que horario se marcaron los asientos
        if len(textoS1_3pm) > 2 : 

                total = precioEntrada*len(textoS1_3pm[2:])
                self.lblDatosSala.setText(textoS1_3pm[0])
                self.lblDatosHorario.setText(textoS1_3pm[1])
                self.lblDatosAsientos.setText(str(textoS1_3pm[2:]))
                self.lblDatosTotal.setText(str(total))

        elif len(textoS1_6pm) > 2 :

                total = precioEntrada*len(textoS1_6pm[2:])
                self.lblDatosSala.setText(textoS1_6pm[0])
                self.lblDatosHorario.setText(textoS1_6pm[1])
                self.lblDatosAsientos.setText(str(textoS1_6pm[2:]))
                self.lblDatosTotal.setText(str(total))
                
        elif len(textoS1_9pm) > 2 :

                total = precioEntrada*len(textoS1_9pm[2:])
                self.lblDatosSala.setText(textoS1_9pm[0])
                self.lblDatosHorario.setText(textoS1_9pm[1])
                self.lblDatosAsientos.setText(str(textoS1_9pm[2:]))
                self.lblDatosTotal.setText(str(total))

 #   def finSalir(self):    (la idea era que se cerraran todas las ventanas menos la principal)

 #       from VentanaAsientos import VentanaAsientosS1_3pm

 #       VentanaAsientosS1_3pm.close()

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeResCom = QtWidgets.QDialog()
    ui = VentanaResCom()
    ui.setupResCom(VentanaDeResCom)
    VentanaDeResCom.show()
    sys.exit(app.exec())
