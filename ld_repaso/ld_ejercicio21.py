from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio21 import Dyr

class dialogo_ej21(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio21.ui",self)
        
        self.btn_calcular.clicked.connect(self.calcular)
        
    def calcular(self):
        dyr=Dyr()
        dyr.p=float(self.ent_p.text())
        dyr.s=float(self.ent_s.text())
        cociente=dyr.calcular_cociente()
        resta=dyr.calcular_resta()
        self.lbl_d.setText(str(cociente))
        self.lbl_r.setText(str(resta))