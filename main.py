import sys
from PyQt5.QtWidgets import QApplication
from clases_load.load_ventana_principal import VentanaPrincipal
from ld_repaso.ld_ventana_principal import VentanaRepaso


def main():
    app = QApplication(sys.argv)
    menu = VentanaRepaso() 
    menu.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()