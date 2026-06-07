from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio5 import Sumatoria

class dialogo_ej5(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio5.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_sumatoria)
        
    def calcular_sumatoria(self):
            ejercicio = Sumatoria()
            ejercicio.n=int(self.ent_n.text())
            resultado = ejercicio.calcular_sumatoria()
            self.lbl_serie.setText(f"Serie={resultado:.2f}")
