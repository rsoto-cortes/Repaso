from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from ld_repaso.ld_ejercicio1 import dialogo_ej1
from ld_repaso.ld_ejercicio2 import dialogo_ej2
from ld_repaso.ld_ejercicio3 import dialogo_ej3
from ld_repaso.ld_ejercicio4 import dialogo_ej4
from ld_repaso.ld_ejercicio5 import dialogo_ej5
from ld_repaso.ld_ejercicio6 import dialogo_ej6
from ld_repaso.ld_ejercicio7 import dialogo_ej7
from ld_repaso.ld_ejercicio8 import dialogo_ej8
from ld_repaso.ld_ejercicio9 import dialogo_ej9
from ld_repaso.ld_ejercicio10 import dialogo_ej10
from ld_repaso.ld_ejercicio11 import dialogo_ej11
from ld_repaso.ld_ejercicio12 import dialogo_ej12
from ld_repaso.ld_ejercicio13 import dialogo_ej13
from ld_repaso.ld_ejercicio14 import dialogo_ej14
from ld_repaso.ld_ejercicio15 import dialogo_ej15
from ld_repaso.ld_ejercicio16 import dialogo_ej16
from ld_repaso.ld_ejercicio17 import dialogo_ej17
from ld_repaso.ld_ejercicio18 import dialogo_ej18
from ld_repaso.ld_ejercicio19 import dialogo_ej19
from ld_repaso.ld_ejercicio20 import dialogo_ej20
from ld_repaso.ld_ejercicio21 import dialogo_ej21
from ld_repaso.ld_ejercicio22 import dialogo_ej22
from ld_repaso.ld_ejercicio23 import dialogo_ej23
from ld_repaso.ld_ejercicio24 import dialogo_ej24
from ld_repaso.ld_ejercicio25 import dialogo_ej25

class VentanaRepaso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/repaso/menu_repaso.ui", self)
        
        self.actionEjercicio1.triggered.connect(self.abrirejercicio1)
        self.actionEjercicio2.triggered.connect(self.abrirejercicio2)
        self.actionEjercicio3.triggered.connect(self.abrirejercicio3)
        self.actionEjercicio4.triggered.connect(self.abrirejercicio4)
        self.actionEjercicio5.triggered.connect(self.abrirejercicio5)
        self.actionEjercicio5_2.triggered.connect(self.abrirejercicio6)
        self.actionEjercicio7.triggered.connect(self.abrirejercicio7)
        self.actionEjercicio8.triggered.connect(self.abrirejercicio8)
        self.actionEjercicio9.triggered.connect(self.abrirejercicio9)
        self.actionEjercicio10.triggered.connect(self.abrirejercicio10)
        self.actionEjercicio11.triggered.connect(self.abrirejercicio11)
        self.actionEjercicio12.triggered.connect(self.abrirejercicio12)
        self.actionEjercicio13.triggered.connect(self.abrirejercicio13)
        self.actionEjercicio14.triggered.connect(self.abrirejercicio14)
        self.actionEjercicio15.triggered.connect(self.abrirejercicio15)
        self.actionEjercicio16.triggered.connect(self.abrirejercicio16)
        self.actionEjercicio17.triggered.connect(self.abrirejercicio17)
        self.actionEjercicio18.triggered.connect(self.abrirejercicio18)
        self.actionEjercicio19.triggered.connect(self.abrirejercicio19)
        self.actionEjercicio20.triggered.connect(self.abrirejercicio20)
        self.actionEjercicio21.triggered.connect(self.abrirejercicio21)
        self.actionEjercicio22.triggered.connect(self.abrirejercicio22)
        self.actionEjercicio23.triggered.connect(self.abrirejercicio23)
        self.actionEjercicio24.triggered.connect(self.abrirejercicio24)
        self.actionEjercicio25.triggered.connect(self.abrirejercicio25)
        self.actionSalir.triggered.connect(self.close)
        
        
    def abrirejercicio1(self):
        dialogo=dialogo_ej1()
        dialogo.exec_()

    def abrirejercicio2(self):
        dialogo=dialogo_ej2()
        dialogo.exec_()

    def abrirejercicio3(self):
        dialogo=dialogo_ej3()
        dialogo.exec_()

    def abrirejercicio4(self):
        dialogo=dialogo_ej4()
        dialogo.exec_()

    def abrirejercicio5(self):
        dialogo=dialogo_ej5()
        dialogo.exec_()

    def abrirejercicio6(self):
        dialogo=dialogo_ej6()
        dialogo.exec_()

    def abrirejercicio7(self):
        dialogo=dialogo_ej7()
        dialogo.exec_()

    def abrirejercicio8(self):
        dialogo=dialogo_ej8()
        dialogo.exec_()

    def abrirejercicio9(self):
        dialogo=dialogo_ej9()
        dialogo.exec_()

    def abrirejercicio10(self):
        dialogo=dialogo_ej10()
        dialogo.exec_()

    def abrirejercicio11(self):
        dialogo=dialogo_ej11()
        dialogo.exec_()

    def abrirejercicio12(self):
        dialogo=dialogo_ej12()
        dialogo.exec_()

    def abrirejercicio13(self):
        dialogo=dialogo_ej13()
        dialogo.exec_()

    def abrirejercicio14(self):
        dialogo=dialogo_ej14()
        dialogo.exec_()

    def abrirejercicio15(self):
        dialogo=dialogo_ej15()
        dialogo.exec_()

    def abrirejercicio16(self):
        dialogo=dialogo_ej16()
        dialogo.exec_()

    def abrirejercicio17(self):
        dialogo=dialogo_ej17()
        dialogo.exec_()

    def abrirejercicio18(self):
        dialogo=dialogo_ej18()
        dialogo.exec_()

    def abrirejercicio19(self):
        dialogo=dialogo_ej19()
        dialogo.exec_()

    def abrirejercicio20(self):
        dialogo=dialogo_ej20()
        dialogo.exec_()

    def abrirejercicio21(self):
        dialogo=dialogo_ej21()
        dialogo.exec_()

    def abrirejercicio22(self):
        dialogo=dialogo_ej22()
        dialogo.exec_()

    def abrirejercicio23(self):
        dialogo=dialogo_ej23()
        dialogo.exec_()

    def abrirejercicio24(self):
        dialogo=dialogo_ej24()
        dialogo.exec_()

    def abrirejercicio25(self):
        dialogo=dialogo_ej25()
        dialogo.exec_()