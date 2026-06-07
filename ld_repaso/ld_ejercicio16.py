from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio16 import Palabra3

class dialogo_ej16(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio16.ui",self)
        
        self.btn_escanear.clicked.connect(self.imprimir_frase)
        
    def imprimir_frase(self):
        palabra=Palabra3()
        palabra.p=self.ent_p.text()
        palabra.l=self.ent_l.text()
        resultado=palabra.imprimir_frase()
        self.lbl_resultado.setText(resultado)