class Cliente(object):


    def __init__(self, nom):
        self.nombre = nom
        self.monto = 0

    def depositar(self, m):
        self.monto = self.monto + m

    def extraer(self, m):
        self.monto = self.monto - m
      

    def obtener_monto(self):
        return self.monto

    def imprimir(self):
        print self.nombre + ' tine depositado la suma de ' + repr(self.monto)
