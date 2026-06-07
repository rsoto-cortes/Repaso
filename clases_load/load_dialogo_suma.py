from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.basicos.calculadora import Calculadora

class DialogoSuma(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_suma.ui", self)
        
        #enlsamos el evento con el boton
        self.btn_sumar.clicked.connect(self.calcularSuma)
        
    def calcularSuma(self):
        casio= Calculadora()
        casio.numero1 = int(self.txt_numero1.text())
        casio.numero2 = int(self.txt_numero2.text())
        casio.calcularSuma()
        self.lbl_resultado.setText(f"{casio.suma}")

