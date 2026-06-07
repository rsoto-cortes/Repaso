class Punto:
    def __init__(self):
        self.cx = 0
        self.cy = 0
        self.px = 0
        self.py = 0
        self.r = 0
        
    def calcular_punto(self):
        distancia = ((self.px - self.cx) ** 2 + (self.py - self.cy) ** 2) ** 0.5
        if distancia < self.r:
            return "El punto está dentro del círculo"
        elif distancia == self.r:
            return "El punto está en la circunferencia"
        else:
            return "El punto está fuera del círculo"