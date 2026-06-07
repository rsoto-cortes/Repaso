from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio22 import Ahorro

class dialogo_ej22(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio22.ui",self)
        
        self.btn_calcular.clicked.connect(self.calcular)
        
    def calcular(self):
        ahorro=Ahorro()
        ahorro.cantidad=float(self.ent_ah.text())
        resultado=ahorro.calcula_ahorro()
        self.lbl_resultado.setText("\n".join(resultado))
