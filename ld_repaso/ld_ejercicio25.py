from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio25 import Invertir

class dialogo_ej25(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio25.ui", self)
        
        self.btn_invertir.clicked.connect(self.invertir_palabra)

    def invertir_palabra(self):
        invertir = Invertir()
        invertir.palabra = self.ent_p.text()
        resultado=invertir.invertir_palabra()
        self.lbl_resultado.setText(f"La palabra invertida es: {resultado}")
