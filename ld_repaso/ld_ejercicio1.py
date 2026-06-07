from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.basicos.ejercicio1 import Pendiente

class dialogo_ej1(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio1.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_pendiente)
        
    def calcular_pendiente(self):
           
        
            ejercicio = Pendiente()
            ejercicio.x1=float(self.ent_x1.text())
            ejercicio.y1=float(self.ent_y1.text())
            ejercicio.x2=float(self.ent_x2.text())
            ejercicio.y2=float(self.ent_y2.text())
            Resultado=ejercicio.calcular_pendiente()
            self.lbl_m.setText(f"m={Resultado}")
            
       