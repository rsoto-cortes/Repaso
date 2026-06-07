class Calcular_Fx:
    def __init__(self):
        self.x = 0
        self.u= 0
        self.a= 0
        self.fx = 0
        
    def calcular_Fx(self):
        self.fx = (1/(2*3.1416*self.a)**(1/2))*(2.71828)**((((self.x-self.u)/self.a)**2)*(0.5))
        return self.fx
        