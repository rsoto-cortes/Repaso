from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio17 import Divison

class dialogo_ej17(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio17.ui",self)
        
        self.btn_calcular.clicked.connect(self.dividir_numeros)
        
    def dividir_numeros(self):
        division=Divison()
        division.num1=float(self.ent_n1.text())
        division.num2=float(self.ent_n2.text())
        resultado=division.dividir()
        self.lbl_resultado.setText(str(resultado))