from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio19 import Saludo

class dialogo_ej19(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio19.ui",self)
        
        self.btn_saludar.clicked.connect(self.saludar)
        
    def saludar(self):
        saludo=Saludo()
        saludo.nombre=self.ent_nom.text()
        resultado=saludo.saludar()
        self.lbl_saludo.setText(str(resultado))