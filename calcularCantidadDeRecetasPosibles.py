receta = {}
ingredientes = {}
while True:
	print("Escribe los ingredientes de la receta. Presiona 'q' si terminaste de listarlos.")
	i = input("Dime el nombre del ingrediente: ")
	if i.lower() == "q":
		break
	receta[i] = int(input("Dime la cantidad de ese ingrediente (sin unidades): "))
print("-----------------------------------\n")
while True:
	print("Escribe los ingredientes que tienes. Presiona 'q' si terminaste de listarlos.")
	i = input("Dime el nombre del ingrediente: ")
	if i.lower() == "q":
		break
	ingredientes[i] = int(input("Dime la cantidad de ese ingrediente (sin unidades): "))

def cakes(receta, ingredientes):
	r = []
	for i in receta:
		r.append(ingredientes.get(i, 0) // receta.get(i))
	return min(r)

print("Puedes realizar esta receta", str(cakes(receta, ingredientes)), "veces.")