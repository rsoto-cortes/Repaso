class Edad:
    def __init__(self):
        self.edad = 0
        self.precio = 0
        

    def calcular_precio(self):
        if self.edad < 4:
            self.precio = 0
        elif self.edad >= 4 and self.edad <= 18:
            self.precio = 5
        else:
            self.precio = 10
        return f"El precio de su entrada es: {self.precio}"
