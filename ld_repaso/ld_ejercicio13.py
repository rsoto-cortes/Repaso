from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio13 import Inversion

class dialogo_ej13(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio13.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_inversion)
        
    def calcular_inversion(self):
            inversion = Inversion()
            inversion.c = float(self.ent_inv.text())
            inversion.i = float(self.ent_int.text())
            inversion.a = int(self.ent_a.text())
            resultado=inversion.calcular_inversion()
            self.lbl_inversion.setText(f"La cantidad de su inversion es de: {resultado:.2f}")