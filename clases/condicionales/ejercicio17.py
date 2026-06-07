class Divison:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def dividir(self):
        if self.num2 == 0:
            return "Error: No se puede dividir por cero."
        else:
            return f"El resultado de dividir {self.num1} entre {self.num2} es: {self.num1 / self.num2}"