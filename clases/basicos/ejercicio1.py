class Pendiente:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.pendiente = 0
        
    def calcular_pendiente(self):
        if self.x2 - self.x1 == 0:
            return "La pendiente es indefinida (línea vertical)"
        else:
            self.pendiente = (self.y2 - self.y1) / (self.x2 - self.x1)
            return self.pendiente