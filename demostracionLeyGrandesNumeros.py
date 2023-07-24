import random

ddd = []
for i in range(6):
	ddd.append({
	0:1,
	1:1,
	2:1,
	3:1,
	4:1,
	5:1,
	6:1,
	7:1,
	8:0,
	9:0,
}[random.randint(0,9)])

print("Probabilidad estimada: 0.8\n")
print("Cantidad de pruebas: 6")
x=ddd.count(1)
print("Cantidad de unos:", str(x))
z=ddd.count(0)
print("Cantidad de ceros:", str(z))
print("Probabilidad calculada:", str(x/6))

print("--------")

a = []
for i in range(1000000):
	a.append({
	0:1,
	1:1,
	2:1,
	3:1,
	4:1,
	5:1,
	6:1,
	7:1,
	8:0,
	9:0,
}[random.randint(0,9)])

print("Cantidad de pruebas: 1000000")
x=a.count(1)
print("Cantidad de unos:", str(x))
z=a.count(0)
print("Cantidad de ceros:", str(z))
print("Probabilidad calculada:", str(x/1000000))