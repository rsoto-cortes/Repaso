from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio7 import Tabla

class dialogo_ej7(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio7.ui", self)
        
        self.btn_generar.clicked.connect(self.generar_tabla)
        
    def generar_tabla(self):
            ejercicio = Tabla()
            ejercicio.n=int(self.ent_num.text())
            resultado=ejercicio.generar_tabla()
            self.lbl_tabla.setText(resultado)
            
