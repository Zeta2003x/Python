class Coche():
	
	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False
		
	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if self.__enmarcha:
			return "ESTA EN MARCHA"
		else:
			return"ESTA PARADO"

	def estado(self):
		print("el coche tiene ", self.__ruedas, " ruedas. Un ancho de ",
			self.__anchoChasis, " y un largo de ", self.__largoChasis)

miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("----------a continuacion creamos el segundo objeto--------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()