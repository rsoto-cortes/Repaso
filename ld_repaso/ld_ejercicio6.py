from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio6 import Sumatoria2

class dialogo_ej6(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio6.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_sumatoria)
        
    def calcular_sumatoria(self):
            ejercicio = Sumatoria2()
            ejercicio.n=int(self.ent_n.text())
            resultado = ejercicio.calcular_sumatoria()
            self.lbl_serie.setText(f"Serie={resultado}")
