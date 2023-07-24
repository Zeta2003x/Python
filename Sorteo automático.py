from random import randint
from tkinter import *

def ruletaDeNombres(cantDePersonas):
	numero = randint(1,cantDePersonas)
	print("Salió el número", str(numero))

while True:
	print("¿Cuántas personas participan del sorteo?")
	try:
		while True:
			n = int(input())
			if n > 0:
				break
			print("Escribe un número mayor a 0")

	except ValueError:
		print("Escribe un número natural.\n")
		continue
	ruletaDeNombres(n)
	print("")
