from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio18 import Grupo 

class dialogo_ej18(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio18.ui",self)
        
        self.btn_buscar.clicked.connect(self.calcular_grupo)
        
    def calcular_grupo(self):
        grupo=Grupo()
        grupo.n=self.ent_n.text()
        grupo.s=self.ent_s.text()
        resultado=grupo.determinar_grupo()
        self.lbl_resultado.setText(str(resultado))