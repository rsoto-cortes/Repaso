from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.basicos.ejercicio3 import Calcular_Fx

class dialogo_ej3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio3.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_Fx)
        
    def calcular_Fx(self):
            ejercicio = Calcular_Fx()
            ejercicio.x=float(self.ent_x.text())
            ejercicio.u=float(self.ent_u.text())
            ejercicio.a=float(self.ent_a.text())
            resultado = ejercicio.calcular_Fx()
            self.lbl_fx.setText(f"Fx={resultado:.2f}")