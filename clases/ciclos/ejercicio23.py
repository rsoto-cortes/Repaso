class Barras:
    def __init__(self):
        self.barras = 0
        self.precio = 0
        self.descuento = 0
        self.coste_final = 0
        
    
    def calcular_precio(self):
        lista = []
        self.precio = self.barras * 3.49
        lista.append(f"El precio de su compra es: {self.precio:.2f}")
        
        self.descuento = self.precio * 0.6
        lista.append(f"El descuento es: {self.descuento:.2f}")

        self.coste_final = self.precio - self.descuento
        lista.append(f"El total final a pagar es de: {self.coste_final:.2f}")
        return lista
    
        
