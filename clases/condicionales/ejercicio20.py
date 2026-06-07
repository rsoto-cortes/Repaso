class Imc:
    def __init__(self):
        self.peso=""
        self.altura=""
    
    
    def calcular_imc(self):
        self.imc=self.peso/(self.altura**2)


        if self.imc<18.5:
            return f"Su IMC es {self.imc:.2f} - Bajo peso"
        elif self.imc>=18.5 and self.imc<=24.9:
            return f"Su IMC es {self.imc:.2f} - Normal"
        elif self.imc>=25 and self.imc<=29.9:
            return f"Su IMC es {self.imc:.2f} - Sobrepeso"
        else:
            return f"Su IMC es {self.imc:.2f} - Obesidad"