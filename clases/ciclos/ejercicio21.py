class Dyr:
    def __init__(self):
        self.p=0
        self.s=0
        self.c=0
        self.r=0
    
    
    def calcular_cociente(self):
        self.c=self.p/self.s
        return f"El resultado de la division es: {self.c}"

    def calcular_resta(self):
        self.r=self.p-self.s
        return f"El resultado de la resta es: {self.r}"
   