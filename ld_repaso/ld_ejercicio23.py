from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio23 import Barras

class dialogo_ej23(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio23.ui",self)
        
        self.btn_calcular.clicked.connect(self.calcular)
        
    def calcular(self):
        barras=Barras()
        barras.barras=int(self.ent_b.text())
        resultado=barras.calcular_precio()
        self.lbl_resultado.setText("\n".join(resultado))