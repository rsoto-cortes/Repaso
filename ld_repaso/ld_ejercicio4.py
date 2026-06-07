from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.condicionales.ejercicio4 import Punto


class dialogo_ej4(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio4.ui", self)
        
        self.btn_calcular.clicked.connect(self.calcular_punto)
        
    def calcular_punto(self):
            ejercicio = Punto()
            ejercicio.cx=float(self.ent_cx.text())
            ejercicio.cy=float(self.ent_cy.text())
            ejercicio.px=float(self.ent_px.text())
            ejercicio.py=float(self.ent_py.text())
            ejercicio.r=float(self.ent_r.text())
            resultado = ejercicio.calcular_punto()
            self.lbl_d.setText(resultado)