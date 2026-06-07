class Palabra3:
    def __init__(self):
        self.p=""
        self.l=""
        self.c=0
        
    def imprimir_frase(self):
        for i in self.p:
            if i == self.l:
                self.c+=1
        return f"La letra {self.l} aparece {self.c} veces en la frase"

  