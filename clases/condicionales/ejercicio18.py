class Grupo:
    def __init__(self):
        self.n=""
        self.s=""
        
    def determinar_grupo(self):
        if self.s.lower() == "femenino":
            if self.n[0].lower() < "m":
                return "Perteneces al grupo A"
            elif self.n[0].lower() >= "m":
                return "Perteneces al grupo B"

        elif self.s.lower() == "masculino":
            if self.n[0].lower() >= "m":
                return "Perteneces al grupo A"
            elif self.n[0].lower() < "m":
                return "Perteneces al grupo B"
    
