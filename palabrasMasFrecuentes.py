def top_n_words(text, cant):
	a = text.split()
	c = 0
	for word in a:
		for l in range(len(word)):
			if not (word[l].isalpha() or word[l] == "'"):
				a.append(word[l+1:])
				a[c] = word[:l]
				break
		c += 1
	a.sort()
	a = a[::-1]
	for word in range(len(a)-1, -1, -1):
		if a[word] == "" or len(a[word]) == a[word].count("'"):
			a.pop(word)
	dic = {}
	for word in a:
		dic[word] = a.count(word)
	res = []
	for i in range(min(cant, len(dic))):
		o = [(value, key) for key, value in dic.items()]
		v, k = max(o)
		res.append(k + ": "+ str(v))
		dic.pop(k)
	return "\n".join(res) + "\n--------------\nCantidad de palabras: " + str(len(a))

while True:
	texto = input("Pega el texto que deseas analizar: ")
	print("\n")
	while True:
		cantidad = input("Indica la cantidad de palabras más frecuentes que quieres saber: ")
		try:		
			cantidad = int(cantidad)
			break
		except ValueError:
			print("Escribe un numero entero, por ejemplo: 1, 69, 420")
	print("\n\n--------------")
	print(top_n_words(texto, cantidad))
	print("--------------")
	denuevo = input("\nSi deseas salir escribe 'Q'.\nSi deseas continuar simplemente pulsa la tecla 'Enter'\n")
	if denuevo.lower() == "q":
		break