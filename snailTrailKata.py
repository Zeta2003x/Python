array= [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]

brray = [[1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]]

crray = [[1,2,3],
         [8,9,4],
         [7,6,5]]

drray = [[1,2],
         [4,3]]

erray = [[1]]

frray = [[]]

def snail(s):
	a = []
	if len(s) == 1:
		return s[0]
	for t in range(int(len(s)/2)):
		for i in s[0]:
			a.append(i)
		s.pop(0)
		for row in range(len(s)-1):
			a.append(s[row][-1])
			s[row].pop(-1)
		s[-1].reverse()
		for i in s[-1]:
			a.append(i)
		s.pop(-1)
		for row in range(len(s)-1, -1, -1):
			a.append(s[row][0])
			s[row].pop(0)
	if len(s) != 0:
		a.append(s[0][0])
	return a

print(snail(array), end="\n---------------\n")
print(snail(brray), end="\n---------------\n")
print(snail(crray), end="\n---------------\n")
print(snail(drray), end="\n---------------\n")
print(snail(erray), end="\n---------------\n")
print(snail(frray), end="\n---------------\n")