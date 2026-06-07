import math

class Sumatoria:
    def __init__(self):
        self.n = 0
        self.suma=0

    def calcular_sumatoria(self):
        
        for i in range(1,self.n+1):
            self.suma += 1/(math.sqrt(2*i+1)**2)
        
        return self.suma