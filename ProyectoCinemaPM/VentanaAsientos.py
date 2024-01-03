from PyQt6 import QtCore, QtGui, QtWidgets

#matrices de las salas
sala1_3pm = [
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]
]
sala1_6pm = [
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]
]
sala1_9pm = [
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]
]

#este arreglo se ocupara para mostrar el resumen de compra
textoS1_3pm = ['Sala 1', '3 pm']
class VentanaAsientosS1_3pm(QtWidgets.QDialog):
    
    def setupAsientos(self, VentanaAsientos):

        #se crea la ventana
        VentanaAsientos.resize(500, 550)
        VentanaAsientos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.085, y1:0.0905455, x2:0.716, y2:1, stop:0 rgba(0, 77, 121, 255), stop:0.5 rgba(13, 16, 51, 255), stop:1 rgba(78, 21, 56, 255));")
        VentanaAsientos.setWindowTitle("Asientos Sala 1 3pm")

        #titulo seleccione los asientos
        self.lblSeleccioneAsientos = QtWidgets.QLabel(parent=VentanaAsientos)
        self.lblSeleccioneAsientos.setGeometry(QtCore.QRect(0, 20, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblSeleccioneAsientos.setFont(font)
        self.lblSeleccioneAsientos.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblSeleccioneAsientos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSeleccioneAsientos.setText("Selecciones los asientos")

        #letras que se usan para identificar las filas de asientos
        self.lblLetras = QtWidgets.QLabel(parent=VentanaAsientos)
        self.lblLetras.setGeometry(QtCore.QRect(70, 220, 49, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblLetras.setFont(font)
        self.lblLetras.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.lblLetras.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblLetras.setText("<html><head/><body><p>A</p><p>B</p><p>C</p><p>D</p><p>E</p></body></html>")

        #ilustracion de la pantalla para guiar donde se encuentra
        self.lblPantalla = QtWidgets.QLabel(parent=VentanaAsientos)
        self.lblPantalla.setGeometry(QtCore.QRect(130, 179, 240, 20))
        self.lblPantalla.setStyleSheet("background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.lblPantalla.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblPantalla.setText("Pantalla")

        #los checkbox de cada asiento
        self.chbA1 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbA1.setGeometry(QtCore.QRect(160, 230, 31, 16))
        self.chbA1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbA1.clicked.connect(self.selecA1)

        self.chbA2 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbA2.setGeometry(QtCore.QRect(200, 230, 31, 16))
        self.chbA2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbA2.clicked.connect(self.selecA2)

        self.chbA3 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbA3.setGeometry(QtCore.QRect(240, 230, 31, 16))
        self.chbA3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbA3.clicked.connect(self.selecA3)

        self.chbA4 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbA4.setGeometry(QtCore.QRect(280, 230, 31, 16))
        self.chbA4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbA4.clicked.connect(self.selecA4)

        self.chbA5 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbA5.setGeometry(QtCore.QRect(320, 230, 31, 16))
        self.chbA5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbA5.clicked.connect(self.selecA5)

        self.chbB1 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbB1.setGeometry(QtCore.QRect(160, 265, 31, 16))
        self.chbB1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbB1.clicked.connect(self.selecB1)

        self.chbB2 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbB2.setGeometry(QtCore.QRect(200, 265, 31, 16))
        self.chbB2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbB2.clicked.connect(self.selecB2)

        self.chbB3 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbB3.setGeometry(QtCore.QRect(240, 265, 31, 16))
        self.chbB3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbB3.clicked.connect(self.selecB3)

        self.chbB4 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbB4.setGeometry(QtCore.QRect(280, 265, 31, 16))
        self.chbB4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbB4.clicked.connect(self.selecB4)

        self.chbB5 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbB5.setGeometry(QtCore.QRect(320, 265, 31, 16))
        self.chbB5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbB5.clicked.connect(self.selecB5)

        self.chbC1 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbC1.setGeometry(QtCore.QRect(160, 303, 31, 16))
        self.chbC1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbC1.clicked.connect(self.selecC1)

        self.chbC2 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbC2.setGeometry(QtCore.QRect(200, 303, 31, 16))
        self.chbC2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbC2.clicked.connect(self.selecC2)

        self.chbC3 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbC3.setGeometry(QtCore.QRect(240, 303, 31, 16))
        self.chbC3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbC3.clicked.connect(self.selecC3)

        self.chbC4 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbC4.setGeometry(QtCore.QRect(280, 303, 31, 16))
        self.chbC4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbC4.clicked.connect(self.selecC4)

        self.chbC5 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbC5.setGeometry(QtCore.QRect(320, 303, 31, 16))
        self.chbC5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbC5.clicked.connect(self.selecC5)

        self.chbD1 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbD1.setGeometry(QtCore.QRect(160, 341, 31, 16))
        self.chbD1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbD1.clicked.connect(self.selecD1)

        self.chbD2 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbD2.setGeometry(QtCore.QRect(200, 341, 31, 16))
        self.chbD2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbD2.clicked.connect(self.selecD2)

        self.chbD3 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbD3.setGeometry(QtCore.QRect(240, 341, 31, 16))
        self.chbD3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbD3.clicked.connect(self.selecD3)

        self.chbD4 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbD4.setGeometry(QtCore.QRect(280, 341, 31, 16))
        self.chbD4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbD4.clicked.connect(self.selecD4)

        self.chbD5 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbD5.setGeometry(QtCore.QRect(320, 341, 31, 16))
        self.chbD5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbD5.clicked.connect(self.selecD5)

        self.chbE1 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbE1.setGeometry(QtCore.QRect(160, 380, 31, 16))
        self.chbE1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbE1.clicked.connect(self.selecE1)

        self.chbE2 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbE2.setGeometry(QtCore.QRect(200, 380, 31, 16))
        self.chbE2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbE2.clicked.connect(self.selecE2)

        self.chbE3 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbE3.setGeometry(QtCore.QRect(240, 380, 31, 16))
        self.chbE3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbE3.clicked.connect(self.selecE3)

        self.chbE4 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbE4.setGeometry(QtCore.QRect(280, 380, 31, 16))
        self.chbE4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbE4.clicked.connect(self.selecE4)

        self.chbE5 = QtWidgets.QCheckBox(parent=VentanaAsientos)
        self.chbE5.setGeometry(QtCore.QRect(320, 380, 31, 16))
        self.chbE5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""color: rgb(255, 255, 255);")
        self.chbE5.clicked.connect(self.selecE5)

        #el texto que muestra cada checbox, en este caso los numeros para identificar la columna del asiento
        self.chbA1.setText("1")
        self.chbA2.setText("2")
        self.chbA3.setText("3")
        self.chbA4.setText("4")
        self.chbA5.setText("5")
        self.chbB3.setText("3")
        self.chbB4.setText("4")
        self.chbB1.setText("1")
        self.chbB5.setText("5")
        self.chbB2.setText("2")
        self.chbC3.setText("3")
        self.chbC4.setText("4")
        self.chbC1.setText("1")
        self.chbC5.setText("5")
        self.chbC2.setText("2")
        self.chbD3.setText("3")
        self.chbD4.setText("4")
        self.chbD1.setText("1")
        self.chbD5.setText("5")
        self.chbD2.setText("2")
        self.chbE3.setText("3")
        self.chbE4.setText("4")
        self.chbE1.setText("1")
        self.chbE5.setText("5")
        self.chbE2.setText("2")

        #boton confirmar
        self.btnConfirmar = QtWidgets.QPushButton(parent=VentanaAsientos)
        self.btnConfirmar.setGeometry(QtCore.QRect(189, 460, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConfirmar.setFont(font)
        self.btnConfirmar.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius:20px\n""")
        self.btnConfirmar.clicked.connect(self.confirma_asientos)
        self.btnConfirmar.setText("Confirmar")

    #funcion que revisa que asiento fue marcado y asi modificar el arreglo que se usara en la ventan de resumen de compra que se abrirá al presinar el boton confirmar
    def confirma_asientos(self):

        from VentanaResCom import VentanaResCom     #ponemos la importacion aca para evitar circulos de importacion y asi evitar errores.

        for i in range(0,5):     #profe, no se por que funciona si le pongp hasta 5, se supone que si es hasta 5 es 6, y hasta 4 es 5, pero con 4 no me marcaba los asientos 5
            for j in range(0,5):
                if (sala1_3pm[i][j] == 1) and (i == 0 and j == 0):

                    
                    textoS1_3pm.append('A1')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show() 

                elif (sala1_3pm[i][j] == 1) and (i == 0 and j == 1):

                    
                    textoS1_3pm.append('A2')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                
                elif (sala1_3pm[i][j] == 1) and (i == 0 and j == 2):

                    
                    textoS1_3pm.append('A3')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 0 and j == 3):

                    
                    textoS1_3pm.append('A4')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 0 and j == 4):

                    
                    textoS1_3pm.append('A5')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 1 and j == 0):

                    
                    textoS1_3pm.append('B1')
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 1 and j == 1):

                    
                    textoS1_3pm.append('B2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 1 and j == 2):

                    
                    textoS1_3pm.append('B3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 1 and j == 3):

                    
                    textoS1_3pm.append('B4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 1 and j == 4):

                    
                    textoS1_3pm.append('B5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 2 and j == 0):

                    
                    textoS1_3pm.append('C1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 2 and j == 1):

                    
                    textoS1_3pm.append('C2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 2 and j == 2):

                    
                    textoS1_3pm.append('C3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 2 and j == 3):

                    
                    textoS1_3pm.append('C4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 2 and j == 4):

                    
                    textoS1_3pm.append('C5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 3 and j == 0):

                    
                    textoS1_3pm.append('D1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 3 and j == 1):

                    
                    textoS1_3pm.append('D2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                    
                elif (sala1_3pm[i][j] == 1) and (i == 3 and j == 2):

                    
                    textoS1_3pm.append('D3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 3 and j == 3):

                    
                    textoS1_3pm.append('D4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 3 and j == 4):

                    
                    textoS1_3pm.append('D5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 4 and j == 0):

                    
                    textoS1_3pm.append('E1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 4 and j == 1):

                    
                    textoS1_3pm.append('E2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 4 and j == 2):

                    
                    textoS1_3pm.append('E3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 4 and j == 3):

                    
                    textoS1_3pm.append('E4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_3pm[i][j] == 1) and (i == 4 and j == 4):

                    
                    textoS1_3pm.append('E5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
    
    #las siguientes funcuiones cambian el valor de la matriz de los asientos, dependiendo de que asientos es marcado
    def selecA1(self):

        if self.chbA1.isChecked():

            sala1_3pm[0][0] = 1
            self.chbA1.setEnabled(False) #esto hace que se inhabilite el checkbox al ser guardado, lamentablemente no se guarda esto al cerrar la ventana ya que al abrirla otra vez, el checkbox esta habilitado

        else:

            sala1_3pm[0][0] = 0 
        

    def selecA2(self):

        if self.chbA2.isChecked():
            sala1_3pm[0][1] = 1
            self.chbA2.setEnabled(False)
        else:
            sala1_3pm[0][1] = 0   
        

    def selecA3(self):

        if self.chbA3.isChecked():
            sala1_3pm[0][2] = 1
            self.chbA3.setEnabled(False)
        else:
            sala1_3pm[0][2] = 0   
        

    def selecA4(self):

        if self.chbA4.isChecked():
            sala1_3pm[0][3] = 1
            self.chbA4.setEnabled(False)
        else:
            sala1_3pm[0][3] = 0   
        

    def selecA5(self):

        if self.chbA5.isChecked():
            sala1_3pm[0][4] = 1
            self.chbA5.setEnabled(False)
        else:
            sala1_3pm[0][4] = 0   


    def selecB1(self):

        if self.chbB1.isChecked():
            self.chbB1.setEnabled(False)
            sala1_3pm[1][0] = 1
        else:
            sala1_3pm[1][0] = 0   


    def selecB2(self):
        
        if self.chbB2.isChecked():
            sala1_3pm[1][1] = 1
            self.chbB2.setEnabled(False)
        else:
            sala1_3pm[1][1] = 0   


    def selecB3(self):
        
        if self.chbB3.isChecked():
            sala1_3pm[1][2] = 1
            self.chbB3.setEnabled(False)
        else:
            sala1_3pm[1][2] = 0   


    def selecB4(self):
        
        if self.chbB4.isChecked():
            self.chbB4.setEnabled(False)
            sala1_3pm[1][3] = 1
        else:
            sala1_3pm[1][3] = 0   
        

    def selecB5(self):
        
        if self.chbB5.isChecked():
            self.chbB5.setEnabled(False)
            sala1_3pm[1][4] = 1
        else:
            sala1_3pm[1][4] = 0   
        

    def selecC1(self):
        
        if self.chbC1.isChecked():
            sala1_3pm[2][0] = 1
            self.chbC1.setEnabled(False)
        else:
            sala1_3pm[2][0] = 0   
        

    def selecC2(self):

        if self.chbC2.isChecked():
            sala1_3pm[2][1] = 1
            self.chbC2.setEnabled(False)
        else:
            sala1_3pm[2][1] = 0   
        

    def selecC3(self):
        
        if self.chbC3.isChecked():
            sala1_3pm[2][2] = 1
            self.chbC3.setEnabled(False)
        else:
            sala1_3pm[2][2] = 0   
        

    def selecC4(self):
        
        if self.chbC4.isChecked():
            sala1_3pm[2][3] = 1
            self.chbC4.setEnabled(False)
        else:
            sala1_3pm[2][3] = 0   
        

    def selecC5(self):

        if self.chbC5.isChecked():
            sala1_3pm[2][4] = 1
            self.chbC5.setEnabled(False)
        else:
            sala1_3pm[2][4] = 0   
        

    def selecD1(self):

        if self.chbD1.isChecked():
            sala1_3pm[3][0] = 1
            self.chbD1.setEnabled(False)
        else:
            sala1_3pm[3][0] = 0   
        

    def selecD2(self):
        
        if self.chbD2.isChecked():
            sala1_3pm[3][1] = 1
            self.chbD2.setEnabled(False)
        else:
            sala1_3pm[3][1] = 0   
        

    def selecD3(self):

        if self.chbD3.isChecked():
            sala1_3pm[3][2] = 1
            self.chbD3.setEnabled(False)
        else:
            sala1_3pm[3][2] = 0   
        

    def selecD4(self):
        
        if self.chbD4.isChecked():
            sala1_3pm[3][3] = 1
            self.chbD4.setEnabled(False)
        else:
            sala1_3pm[3][3] = 0   
        

    def selecD5(self):

        if self.chbD5.isChecked():
            sala1_3pm[3][4] = 1
            self.chbD5.setEnabled(False)
        else:
            sala1_3pm[3][4] = 0   
        

    def selecE1(self):
        
        if self.chbE1.isChecked():
            sala1_3pm[4][0] = 1
            self.chbE1.setEnabled(False)
        else:
            sala1_3pm[4][0] = 0   
        
        
    def selecE2(self):
        
        if self.chbE2.isChecked():
            sala1_3pm[4][1] = 1
            self.chbE2.setEnabled(False)
        else:
            sala1_3pm[4][1] = 0   
        

    def selecE3(self):
        
        if self.chbE3.isChecked():
            sala1_3pm[4][2] = 1
            self.chbE3.setEnabled(False)
        else:
            sala1_3pm[4][2] = 0   
        

    def selecE4(self):

        if self.chbE4.isChecked():
            sala1_3pm[4][3] = 1
            self.chbE4.setEnabled(False)
        else:
            sala1_3pm[4][3] = 0   
        

    def selecE5(self):

        if self.chbE5.isChecked():
            sala1_3pm[4][4] = 1
            self.chbE5.setEnabled(False)
        else:
            sala1_3pm[4][4] = 0   
        
#este arreglo se ocupara para mostrar el resumen de compra
textoS1_6pm = ['Sala 1', '6 pm']
class VentanaAsientosS1_6pm(VentanaAsientosS1_3pm):
    
    def setupAsientos(self, VentanaAsientos):
        return super().setupAsientos(VentanaAsientos)
    
    def confirma_asientos(self):

        from VentanaResCom import VentanaResCom

        for i in range(0,5):
            for j in range(0,5):
                if (sala1_6pm[i][j] == 1) and (i == 0 and j == 0):

                    

                    textoS1_6pm.append('A1')
                    

                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show() 

                elif (sala1_6pm[i][j] == 1) and (i == 0 and j == 1):

                    
                    textoS1_6pm.append('A2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                
                elif (sala1_6pm[i][j] == 1) and (i == 0 and j == 2):

                    
                    textoS1_6pm.append('A3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 0 and j == 3):

                    
                    textoS1_6pm.append('A4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 0 and j == 4):

                    
                    textoS1_6pm.append('A5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 1 and j == 0):

                    
                    textoS1_6pm.append('B1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 1 and j == 1):

                    
                    textoS1_6pm.append('B2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 1 and j == 2):

                    
                    textoS1_6pm.append('B3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 1 and j == 3):

                    
                    textoS1_6pm.append('B4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 1 and j == 4):

                    
                    textoS1_6pm.append('B5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 2 and j == 0):

                    
                    textoS1_6pm.append('C1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 2 and j == 1):

                    
                    textoS1_6pm.append('C2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 2 and j == 2):

                    
                    textoS1_6pm.append('C3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 2 and j == 3):

                    
                    textoS1_6pm.append('C4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 2 and j == 4):

                    
                    textoS1_6pm.append('C5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 3 and j == 0):

                    
                    textoS1_6pm.append('D1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 3 and j == 1):

                    
                    textoS1_6pm.append('D2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                    
                elif (sala1_6pm[i][j] == 1) and (i == 3 and j == 2):

                    
                    textoS1_6pm.append('D3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 3 and j == 3):

                    
                    textoS1_6pm.append('D4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 3 and j == 4):

                    
                    textoS1_6pm.append('D5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 4 and j == 0):

                    
                    textoS1_6pm.append('E1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 4 and j == 1):

                    
                    textoS1_6pm.append('E2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 4 and j == 2):

                    
                    textoS1_6pm.append('E3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 4 and j == 3):

                    
                    textoS1_6pm.append('E4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_6pm[i][j] == 1) and (i == 4 and j == 4):

                    
                    textoS1_6pm.append('E5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

    def selecA1(self):

        if self.chbA1.isChecked():

            sala1_6pm[0][0] = 1
            self.chbA1.setEnabled(False)

        else:

            sala1_6pm[0][0] = 0 
    

    def selecA2(self):

        if self.chbA2.isChecked():
            sala1_6pm[0][1] = 1
            self.chbA2.setEnabled(False)
        else:
            sala1_6pm[0][1] = 0   


    def selecA3(self):

        if self.chbA3.isChecked():
            sala1_6pm[0][2] = 1
            self.chbA3.setEnabled(False)
        else:
            sala1_6pm[0][2] = 0   


    def selecA4(self):

        if self.chbA4.isChecked():
            sala1_6pm[0][3] = 1
            self.chbA4.setEnabled(False)
        else:
            sala1_6pm[0][3] = 0   


    def selecA5(self):

        if self.chbA5.isChecked():
            sala1_6pm[0][4] = 1
            self.chbA5.setEnabled(False)
        else:
            sala1_6pm[0][4] = 0   


    def selecB1(self):

        if self.chbB1.isChecked():
            sala1_6pm[1][0] = 1
            self.chbB1.setEnabled(False)
        else:
            sala1_6pm[1][0] = 0   


    def selecB2(self):
        
        if self.chbB2.isChecked():
            sala1_6pm[1][1] = 1
            self.chbB2.setEnabled(False)
        else:
            sala1_6pm[1][1] = 0   


    def selecB3(self):
        
        if self.chbB3.isChecked():
            sala1_6pm[1][2] = 1
            self.chbB3.setEnabled(False)
        else:
            sala1_6pm[1][2] = 0   


    def selecB4(self):
        
        if self.chbB4.isChecked():
            sala1_6pm[1][3] = 1
            self.chbB4.setEnabled(False)
        else:
            sala1_6pm[1][3] = 0   
        

    def selecB5(self):
        
        if self.chbB5.isChecked():
            sala1_6pm[1][4] = 1
            self.chbB5.setEnabled(False)
        else:
            sala1_6pm[1][4] = 0   
        

    def selecC1(self):
        
        if self.chbC1.isChecked():
            sala1_6pm[2][0] = 1
            self.chbC1.setEnabled(False)
        else:
            sala1_6pm[2][0] = 0   
        

    def selecC2(self):

        if self.chbC2.isChecked():
            sala1_6pm[2][1] = 1
            self.chbC2.setEnabled(False)
        else:
            sala1_6pm[2][1] = 0   
        

    def selecC3(self):
        
        if self.chbC3.isChecked():
            sala1_6pm[2][2] = 1
            self.chbC3.setEnabled(False)
        else:
            sala1_6pm[2][2] = 0   
        

    def selecC4(self):
        
        if self.chbC4.isChecked():
            sala1_6pm[2][3] = 1
            self.chbC4.setEnabled(False)
        else:
            sala1_6pm[2][3] = 0   
        

    def selecC5(self):

        if self.chbC5.isChecked():
            sala1_6pm[2][4] = 1
            self.chbC5.setEnabled(False)
        else:
            sala1_6pm[2][4] = 0   
        

    def selecD1(self):

        if self.chbD1.isChecked():
            sala1_6pm[3][0] = 1
            self.chbD1.setEnabled(False)
        else:
            sala1_6pm[3][0] = 0   
        

    def selecD2(self):
        
        if self.chbD2.isChecked():
            sala1_6pm[3][1] = 1
            self.chbD2.setEnabled(False)
        else:
            sala1_6pm[3][1] = 0   
        

    def selecD3(self):

        if self.chbD3.isChecked():
            sala1_6pm[3][2] = 1
            self.chbD3.setEnabled(False)
        else:
            sala1_6pm[3][2] = 0   
        

    def selecD4(self):
        
        if self.chbD4.isChecked():
            sala1_6pm[3][3] = 1
            self.chbD4.setEnabled(False)
        else:
            sala1_6pm[3][3] = 0   
        

    def selecD5(self):

        if self.chbD5.isChecked():
            sala1_6pm[3][4] = 1
            self.chbD5.setEnabled(False)
        else:
            sala1_6pm[3][4] = 0   
        

    def selecE1(self):
        
        if self.chbE1.isChecked():
            sala1_6pm[4][0] = 1
            self.chbE1.setEnabled(False)
        else:
            sala1_6pm[4][0] = 0   
        
        
    def selecE2(self):
        
        if self.chbE2.isChecked():
            sala1_6pm[4][1] = 1
            self.chbE2.setEnabled(False)
        else:
            sala1_6pm[4][1] = 0   
        

    def selecE3(self):
        
        if self.chbE3.isChecked():
            sala1_6pm[4][2] = 1
            self.chbE3.setEnabled(False)
        else:
            sala1_6pm[4][2] = 0   
        

    def selecE4(self):

        if self.chbE4.isChecked():
            sala1_6pm[4][3] = 1
            self.chbE4.setEnabled(False)
        else:
            sala1_6pm[4][3] = 0   
        

    def selecE5(self):

        if self.chbE5.isChecked():
            sala1_6pm[4][4] = 1
            self.chbE5.setEnabled(False)
        else:
            sala1_6pm[4][4] = 0 

#este arreglo se ocupara para mostrar el resumen de compra
textoS1_9pm = ['Sala 1', '9 pm']
class VentanaAsientosS1_9pm(VentanaAsientosS1_3pm):
    
    def setupAsientos(self, VentanaAsientos):

        return super().setupAsientos(VentanaAsientos)
    
    def confirma_asientos(self):

        from VentanaResCom import VentanaResCom

        for i in range(0,5):
            for j in range(0,5):
                if (sala1_9pm[i][j] == 1) and (i == 0 and j == 0):

                    

                    textoS1_9pm.append('A1')
                    

                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show() 

                elif (sala1_9pm[i][j] == 1) and (i == 0 and j == 1):

                    
                    textoS1_9pm.append('A2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                
                elif (sala1_9pm[i][j] == 1) and (i == 0 and j == 2):

                    
                    textoS1_9pm.append('A3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 0 and j == 3):

                    
                    textoS1_9pm.append('A4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 0 and j == 4):

                    
                    textoS1_9pm.append('A5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 1 and j == 0):

                    
                    textoS1_9pm.append('B1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 1 and j == 1):

                    
                    textoS1_9pm.append('B2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 1 and j == 2):

                    
                    textoS1_9pm.append('B3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 1 and j == 3):

                    
                    textoS1_9pm.append('B4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 1 and j == 4):

                    
                    textoS1_9pm.append('B5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 2 and j == 0):

                    
                    textoS1_9pm.append('C1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 2 and j == 1):

                    
                    textoS1_9pm.append('C2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 2 and j == 2):

                    
                    textoS1_9pm.append('C3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 2 and j == 3):

                    
                    textoS1_9pm.append('C4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 2 and j == 4):

                    
                    textoS1_9pm.append('C5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 3 and j == 0):

                    
                    textoS1_9pm.append('D1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 3 and j == 1):

                    
                    textoS1_9pm.append('D2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
                    
                elif (sala1_9pm[i][j] == 1) and (i == 3 and j == 2):

                    
                    textoS1_9pm.append('D3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 3 and j == 3):

                    
                    textoS1_9pm.append('D4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 3 and j == 4):

                    
                    textoS1_9pm.append('D1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 4 and j == 0):

                    
                    textoS1_9pm.append('E1')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 4 and j == 1):

                    
                    textoS1_9pm.append('E2')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 4 and j == 2):

                    
                    textoS1_9pm.append('E3')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 4 and j == 3):

                    
                    textoS1_9pm.append('E4')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()

                elif (sala1_9pm[i][j] == 1) and (i == 4 and j == 4):

                    
                    textoS1_9pm.append('E5')
                    
                    self.ventana_compra = VentanaResCom()
                    self.ventana_compra.setupResCom(self.ventana_compra) 
                    self.ventana_compra.show()
    
    def selecA1(self):

        if self.chbA1.isChecked():

            sala1_9pm[0][0] = 1
            self.chbA1.setEnabled(False)

        else:

            sala1_9pm[0][0] = 0 
    

    def selecA2(self):

        if self.chbA2.isChecked():
            sala1_9pm[0][1] = 1
            self.chbA2.setEnabled(False)
        else:
            sala1_9pm[0][1] = 0   


    def selecA3(self):

        if self.chbA3.isChecked():
            sala1_9pm[0][2] = 1
            self.chbA3.setEnabled(False)
        else:
            sala1_9pm[0][2] = 0   


    def selecA4(self):

        if self.chbA4.isChecked():
            sala1_9pm[0][3] = 1
            self.chbA4.setEnabled(False)
        else:
            sala1_9pm[0][3] = 0   


    def selecA5(self):

        if self.chbA5.isChecked():
            sala1_9pm[0][4] = 1
            self.chbA5.setEnabled(False)
        else:
            sala1_9pm[0][4] = 0   


    def selecB1(self):

        if self.chbB1.isChecked():
            sala1_9pm[1][0] = 1
            self.chbB1.setEnabled(False)
        else:
            sala1_9pm[1][0] = 0   


    def selecB2(self):
        
        if self.chbB2.isChecked():
            sala1_9pm[1][1] = 1
            self.chbB2.setEnabled(False)
        else:
            sala1_9pm[1][1] = 0   


    def selecB3(self):
        
        if self.chbB3.isChecked():
            sala1_9pm[1][2] = 1
            self.chbB3.setEnabled(False)
        else:
            sala1_9pm[1][2] = 0   


    def selecB4(self):
        
        if self.chbB4.isChecked():
            sala1_9pm[1][3] = 1
            self.chbB4.setEnabled(False)
        else:
            sala1_9pm[1][3] = 0   
        

    def selecB5(self):
        
        if self.chbB5.isChecked():
            sala1_9pm[1][4] = 1
            self.chbB5.setEnabled(False)
        else:
            sala1_9pm[1][4] = 0   
        

    def selecC1(self):
        
        if self.chbC1.isChecked():
            sala1_9pm[2][0] = 1
            self.chbC1.setEnabled(False)
        else:
            sala1_9pm[2][0] = 0   
        

    def selecC2(self):

        if self.chbC2.isChecked():
            sala1_9pm[2][1] = 1
            self.chbC2.setEnabled(False)
        else:
            sala1_9pm[2][1] = 0   
        

    def selecC3(self):
        
        if self.chbC3.isChecked():
            sala1_9pm[2][2] = 1
            self.chbC3.setEnabled(False)
        else:
            sala1_9pm[2][2] = 0   
        

    def selecC4(self):
        
        if self.chbC4.isChecked():
            sala1_9pm[2][3] = 1
            self.chbC4.setEnabled(False)
        else:
            sala1_9pm[2][3] = 0   
        

    def selecC5(self):

        if self.chbC5.isChecked():
            sala1_9pm[2][4] = 1
            self.chbC5.setEnabled(False)
        else:
            sala1_9pm[2][4] = 0   
        

    def selecD1(self):

        if self.chbD1.isChecked():
            sala1_9pm[3][0] = 1
            self.chbD1.setEnabled(False)
        else:
            sala1_9pm[3][0] = 0   
        

    def selecD2(self):
        
        if self.chbD2.isChecked():
            sala1_9pm[3][1] = 1
            self.chbD2.setEnabled(False)
        else:
            sala1_9pm[3][1] = 0   
        

    def selecD3(self):

        if self.chbD3.isChecked():
            sala1_9pm[3][2] = 1
            self.chbD3.setEnabled(False)
        else:
            sala1_9pm[3][2] = 0   
        

    def selecD4(self):
        
        if self.chbD4.isChecked():
            sala1_9pm[3][3] = 1
            self.chbD4.setEnabled(False)
        else:
            sala1_9pm[3][3] = 0   
        

    def selecD5(self):

        if self.chbD5.isChecked():
            sala1_9pm[3][4] = 1
            self.chbD5.setEnabled(False)
        else:
            sala1_9pm[3][4] = 0   
        

    def selecE1(self):
        
        if self.chbE1.isChecked():
            sala1_9pm[4][0] = 1
            self.chbE1.setEnabled(False)
        else:
            sala1_9pm[4][0] = 0   
        
        
    def selecE2(self):
        
        if self.chbE2.isChecked():
            sala1_9pm[4][1] = 1
            self.chbE2.setEnabled(False)
        else:
            sala1_9pm[4][1] = 0   
        

    def selecE3(self):
        
        if self.chbE3.isChecked():
            sala1_9pm[4][2] = 1
            self.chbE3.setEnabled(False)
        else:
            sala1_9pm[4][2] = 0   
        

    def selecE4(self):

        if self.chbE4.isChecked():
            sala1_9pm[4][3] = 1
            self.chbE4.setEnabled(False)
        else:
            sala1_9pm[4][3] = 0   
        

    def selecE5(self):

        if self.chbE5.isChecked():
            sala1_9pm[4][4] = 1
            self.chbE5.setEnabled(False)
        else:
            sala1_9pm[4][4] = 0   


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaDeAsientos = QtWidgets.QDialog()
    ui = VentanaAsientosS1_3pm()
    ui.setupAsientos(VentanaDeAsientos)
    VentanaDeAsientos.show()
    sys.exit(app.exec())
