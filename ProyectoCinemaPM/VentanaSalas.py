from PyQt6 import QtCore, QtGui, QtWidgets


class VentanaSalas(QtWidgets.QDialog):

    def setupSalas(self, VentanaSalas):

        #se crea la ventana
        VentanaSalas.resize(500, 550)
        VentanaSalas.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaSalas.setWindowTitle("Salas")

        #titulo Seleccione la sala
        self.lblSeleccioneSala = QtWidgets.QLabel(parent=VentanaSalas)
        self.lblSeleccioneSala.setGeometry(QtCore.QRect(0, 20, 500, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblSeleccioneSala.setFont(font)
        self.lblSeleccioneSala.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblSeleccioneSala.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSeleccioneSala.setText("Seleccione la sala")

        #boton sala 1
        self.btnSala1 = QtWidgets.QPushButton(parent=VentanaSalas)
        self.btnSala1.setGeometry(QtCore.QRect(170, 200, 160, 40))
        self.btnSala1.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius:20px")
        self.btnSala1.clicked.connect(self.abrir_ventana_horariosS1)
        self.btnSala1.setText("Sala 1")

    #funcion que abre la ventana de horarios
    def abrir_ventana_horariosS1(self):

        from VentanaHorarios import VentanaHorarios #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        self.ventana_horarios = VentanaHorarios()
        self.ventana_horarios.setupHorarios(self.ventana_horarios)
        self.ventana_horarios.show()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeSalas = QtWidgets.QDialog()
    ui = VentanaSalas()
    ui.setupSalas(VentanaDeSalas)
    VentanaDeSalas.show()
    sys.exit(app.exec())
