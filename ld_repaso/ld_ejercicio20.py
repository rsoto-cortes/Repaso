from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio20 import Imc

class dialogo_ej20(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio20.ui",self)
        
        self.btn_calcular.clicked.connect(self.calcular_imc)
        
    def calcular_imc(self):
        imc=Imc()
        imc.peso=float(self.ent_p.text())
        imc.altura=float(self.ent_a.text())
        resultado=imc.calcular_imc()
        self.lbl_resultado.setText(str(resultado))
        