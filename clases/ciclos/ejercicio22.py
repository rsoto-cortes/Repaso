class Ahorro:
  def __init__(self):
    self.cantidad=0
    self.primer_año=0
    self.pa=0
    self.segundo_año=0
    self.pb=0
    self.tercer_año=0
    self.pc=0

  def calcula_ahorro(self):
      self.primer_año=self.cantidad*0.04
      self.pa=self.cantidad+self.primer_año
      self.segundo_año=self.pa*0.04
      self.pb=self.pa+self.segundo_año
      self.tercer_año=self.pb*0.04
      self.pc=self.pb+self.tercer_año
      lista = []
      lista.append(f"El ahorro del primer año es: {self.pa:.2f}")
      lista.append(f"El ahorro del segundo año es: {self.pb:.2f}")
      lista.append(f"El ahorro del tercer año es: {self.pc:.2f}")
      return lista
