class Numero3:
    def __init__(self):
        self.n = 0
        
    def imprimir_numero(self):
        if self.n == 1:
            return "El número no es primo"
        elif self.n == 2:
            return "El número es primo"
        else:
            for i in range(2, self.n):
                if self.n % i == 0:
                    return "El número no es primo"
            return "El número es primo"
                

  