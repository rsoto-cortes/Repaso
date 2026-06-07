from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.basicos.ejercicio2 import Distancia

class dialogo_ej2(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio2.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_distancia)
        
    def calcular_distancia(self):
            ejercicio = Distancia()
            ejercicio.x1=float(self.ent_x1.text())
            ejercicio.y1=float(self.ent_y1.text())
            ejercicio.x2=float(self.ent_x2.text())
            ejercicio.y2=float(self.ent_y2.text())
            distancia = ejercicio.calcular_Distancia()
            self.lbl_distancia.setText(f"d={distancia:.2f}")

