class Numero2:
    def __init__(self):
        self.n = 0

    def imprimir_numero(self):
        lista = []
        for i in range(self.n, -1, -1):
            lista.append(str(i))
        return ",".join(lista)
