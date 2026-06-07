class Numero:
    def __init__(self):
        self.n = 0

    def imprimir_numero(self):
        lista=[]
        for i in range(1, self.n + 1, 2):
            lista.append(str(i))
        return ",".join(lista)
