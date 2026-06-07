class Tablas:

    def mostrar_tabla(self):
        lineas = []
        for i in range(1, 11):
            for j in range(1, 11):
                lineas.append(f"{i} x {j} = {i*j}")
            if i != 10:
                lineas.append("")
        return "\n".join(lineas)

