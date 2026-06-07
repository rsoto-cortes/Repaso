from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio11 import Numero

class dialogo_ej11(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio11.ui", self)
        
        self.btn_mostrar.clicked.connect(self.imprimir_numero)
        
    def imprimir_numero(self):
            numero = Numero()
            numero.n = int(self.ent_num.text())
            generar=numero.imprimir_numero()
            self.lbl_resultado.setText(f"Los numeros impares son: {generar}")