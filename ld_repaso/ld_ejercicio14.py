from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio14 import Numero3

class dialogo_ej14(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio14.ui", self)
        
        self.btn_generar.clicked.connect(self.calcular_primo)
        
    def calcular_primo(self):
            numero = Numero3()
            numero.n = int(self.ent_num.text())
            resultado=numero.imprimir_numero()
            self.lbl_resultado.setText(resultado)

