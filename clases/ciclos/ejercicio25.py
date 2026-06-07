class Invertir:
    def __init__(self):
        self.palabra = ""
        self.palabra_invertida = ""
    
    def invertir_palabra(self):
        self.palabra_invertida=self.palabra[::-1]
        return f"La palabra invertida es: {self.palabra_invertida}"
