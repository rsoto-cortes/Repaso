from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio10 import Edad

class dialogo_ej10(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio10.ui", self)
        
        self.btn_generar.clicked.connect(self.imprimir_edad)
        
    def imprimir_edad(self):
            edad = Edad()
            edad.edad = int(self.ent_edad.text())
            generar=edad.imprimir_edad()
            self.lbl_mostrar.setText(str(generar))