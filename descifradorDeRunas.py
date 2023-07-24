def solve_runes(runes):
	if "+" in runes:
		operator = "+"
		runesm = runes.find(operator)
	elif "*" in runes:
		operator = "*"
		runesm = runes.find(operator)
	else:
		operator = "-"
		runesm = runes[1:].find(operator)+1
	a = runes[:runesm]
	b = runes[runesm+1:runes.find("=")]
	c = runes[runes.find("=")+1:]
	numbers = "0123456789"
	if a == "??" or b == "??" or c == "??":
		numbers = "123456789"
	pos = "".join([i for i in numbers if i not in runes])
	for i in pos:
		aa = a.translate(a.maketrans("?", i))
		bb = b.translate(b.maketrans("?", i))
		cc = c.translate(c.maketrans("?", i))
		if operator == "+":
			cuenta = int(aa) + int(bb)
			if cuenta == int(cc):
				return int(i)
		elif operator == "-":
			cuenta = int(aa) - int(bb)
			if cuenta == int(cc):
				return int(i)
		else:
			cuenta = int(aa) * int(bb)
			if cuenta == int(cc):
				return int(i)
	return -1

print(solve_runes("123*4?6=?6088"), end=" should equal: 5\n------------\n")
print(solve_runes("20-1?=3"), end=" should equal: 7\n------------\n")
print(solve_runes("?*11=??"), end=" should equal: 2\n------------\n")