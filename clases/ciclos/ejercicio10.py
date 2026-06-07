class Edad:
    def __init__(self):
        self.edad = 0
        
    def imprimir_edad(self):
        años = []
        for i in range(1,self.edad+1):
            if i==1:
                años.append(f"Haz cumplido {i} año")
            else:
                años.append(f"Haz cumplido {i} años")
        return "\n".join(años)


