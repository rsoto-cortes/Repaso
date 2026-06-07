class Tabla:
    def __init__(self):
        self.n = 0

    def generar_tabla(self):
        lineas = []
        for i in range(1, 11):
            resultado = self.n * i
            lineas.append(f"{self.n} x {i} = {resultado}")
        return "\n".join(lineas)