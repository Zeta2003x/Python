from random import randint

class CaesarCipher(object):

	def __init__(self, shift):
		alphabet = ''.join([chr(i) for i in range(255)])
		self.alpha = alphabet
		self.newalpha = self.alpha[shift:] + self.alpha[:shift]

	def encode(self, str):
		t = str.maketrans(self.alpha, self.newalpha)
		return str.translate(t)

	def decode(self, str):
		t = str.maketrans(self.newalpha, self.alpha)
		return str.translate(t)

c = CaesarCipher(5)
