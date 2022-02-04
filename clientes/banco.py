from cliente import Cliente;

class Banco(object):


    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Edgar ")
        self.cliente3 = Cliente("Jorge")


    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)


    def depositos_totales(self):
        total = self.cliente1.obtener_monto() + self.cliente2.obtener_monto() + self.cliente3.obtener_monto()
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
	print "El total entre los 3 es de: " + repr(total)	
		

banco1 = Banco();
banco1.operar();
banco1.operar();
banco1.depositos_totales();
