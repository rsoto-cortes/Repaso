from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_saludo.ui", self)
        
        
        #enlsamos el evento con el boton
        self.btn_saludar.clicked.connect(self.saludar)
        
    def saludar(self):
        nombre = self.txt_nombre.text()
        saludo = f"¡Hola, {nombre}!"
        self.lbl_saludo.setText(saludo)

