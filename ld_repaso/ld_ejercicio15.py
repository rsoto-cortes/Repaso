from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio15 import Palabra2

class dialogo_ej15(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio15.ui",self)
        
        self.btn_generar.clicked.connect(self.imprimir_palabra)
        
    def imprimir_palabra(self):
        palabra=Palabra2()
        palabra.p=self.ent_p.text()
        resultado=palabra.imprimir_palabra()
        self.lbl_resultado.setText(resultado)