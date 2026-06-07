from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio9 import Palabra

class dialogo_ej9(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio9.ui", self)
        
        self.btn_generar.clicked.connect(self.imprimir_palabra)
        
    def imprimir_palabra(self):
            palabra = Palabra()
            palabra.palabra = self.ent_p.text()
            generar=palabra.imprimir_palabra()
            self.lbl_palabra.setText(str(generar))