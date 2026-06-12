from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from clases.ciclos.ejercicio8 import Tablas

class dialogo_ej8(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/ejercicio8.ui", self)

        self.btn_generar.clicked.connect(self.generar_tabla)
        
    def generar_tabla(self):
        ejercicio = Tablas()
        resultado=ejercicio.mostrar_tabla()
        self.lbl_tablas.setPlainText(resultado)