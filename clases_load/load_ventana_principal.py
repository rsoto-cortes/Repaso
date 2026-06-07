from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from clases_load.load_dialogo import Dialogo
from clases_load.load_dialogo_suma import DialogoSuma

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu_principal.ui", self)
        
        self.actionSaludo.triggered.connect(self.abrirDialogoSaludo)
        self.actionCalculadora.triggered.connect(self.abrirDialogoCalculadora)
        self.actionSalir.triggered.connect(self.close)
        
    def abrirDialogoSaludo(self):
        dialogo = Dialogo()
        dialogo.exec_()
        
    def abrirDialogoCalculadora(self):
        dialogo = DialogoSuma()
        dialogo.exec_()
        
    