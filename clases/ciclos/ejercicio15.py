class Palabra2:
    def __init__(self):
        self.p=""   
        
    def imprimir_palabra(self):
        lista = []
        for letra in self.p:
            lista.append(letra)
        return "\n".join(lista)
