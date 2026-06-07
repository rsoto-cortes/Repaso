from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio12 import Numero2

class dialogo_ej12(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio12.ui", self)
        
        self.btn_generar.clicked.connect(self.imprimir_numero)
        
    def imprimir_numero(self):
            numero = Numero2()
            numero.n = int(self.ent_num.text())
            generar=numero.imprimir_numero()
            self.lbl_mostrar.setText(f"Los numeros del {numero.n} al 0 son: {generar}")