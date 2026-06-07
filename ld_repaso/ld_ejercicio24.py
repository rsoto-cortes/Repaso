from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio24 import Edad

class dialogo_ej24(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio24.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_precio)

    def calcular_precio(self):
        edad = Edad()
        edad.edad = int(self.ent_e.text())
        resultado=edad.calcular_precio()
        self.lbl_resultado.setText(resultado)
