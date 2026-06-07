class Inversion:
    def __init__(self):
        self.c = 0
        self.i = 0
        self.a = 0
        
    def calcular_inversion(self):
        self.c=self.c*(1+self.i)**(self.a)
        return self.c