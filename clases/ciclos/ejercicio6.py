import math

class Sumatoria2:
    def __init__(self):
        self.n = 0
        self.s = 0

    def calcular_sumatoria(self):
        for i in range(1,self.n+1):
            self.s+=(1/math.e)**i
            self.s=self.s/3
            
        return self.s
      