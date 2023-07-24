def parse_molecule(formula):
	resultado = {}
	par = False
	cor = False
	lla = False
	dos = False
	for i in range(len(formula)):
		if formula[i].islower() and not formula[i-1].isupper():
			return "\nHas ingresado una molécula inválida. Las moléculas pueden ser de este estilo:\nUna letra mayúscula: C (Carbono)\nUna letra mayúscula seguida de una minúscula: He (Helio)"
		if formula[i].isupper():
			atomo = formula[i]
			if i+1 == len(formula):
				verKey = resultado.get(atomo, -1)
				if verKey == -1: resultado[atomo] = 1; break
				resultado[atomo] += 1
				break
			if formula[i+1].islower(): atomo = formula[i:i+2]; dos = True
			if resultado.get(atomo, -1) == -1: resultado[atomo] = 0
			if "(" not in formula[i:] and ")" in formula[i:]: par = True
			if "[" not in formula[i:] and "]" in formula[i:]: cor = True
			if "{" not in formula[i:] and "}" in formula[i:]: lla = True
			suma = 1
			for n in range(i, len(formula)):
				if formula[n].isnumeric():
					for papa in range(n+1, len(formula)):
						if not formula[papa].isnumeric():
							numero = formula[n:papa]
							break
					if n == i+1 or (dos and n == i+2): suma = suma*int(numero)
					if formula[n-1] == ")" and par: suma = suma*int(numero)
					if formula[n-1] == "]" and cor: suma = suma*int(numero)
					if formula[n-1] == "}" and lla: suma = suma*int(numero)
			resultado[atomo] += suma
	return resultado

print("Este programa cuenta la cantidad de átomos de cada elemento en la molécula ingresada. Puedes usar paréntesis, corchetes y llaves expresar tu molécula.\nEjemplos:\nH2O ------> {'H': 2, 'O' : 1}\nK4[ON(SO3)2]2 ------> {'K': 4,  'O': 14,  'N': 2,  'S': 4}")

while True:
	print(str(parse_molecule(input("Escribe la molécula que quieres utilizar: "))))
	denuevo = input("\nSi deseas salir escribe 'N'. Si deseas continuar simplemente pulsa la tecla 'Enter'")
	if denuevo.lower() == "n":
		break