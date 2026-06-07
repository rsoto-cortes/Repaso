class Palabra:
    def __init__(self):
        self.palabra = ""
        self.i = 0

    def imprimir_palabra(self):
        lineas = []
        for i in range(10):
            lineas.append(self.palabra)
        return "\n".join(lineas)