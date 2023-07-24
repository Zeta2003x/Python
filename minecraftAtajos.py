import time
import pyautogui
 
pyautogui.press("up")
class minecraft(object):

	def __init__(self, action):
		self.action = action
		if self.action == "Mantener click derecho":self.mClickDer()
		elif self.action == "Repetir click derecho":self.rClickDer()
		else: self.rClickIzq()

	def mClickDer(self):
		pyautogui.mouseDown()
	def rClickDer(self):
		for i in range(5000):
			pyautogui.click(button="right")
			time.sleep(0.8)
			print("golpe n° "+str(i))
	def rClickIzq(self):
		for i in range(5000):
			pyautogui.click()
			time.sleep(0.8)
			print("golpe n° "+str(i))

action = pyautogui.confirm(title="", text="Elige la opción que deseas realizar", buttons=["Mantener click derecho","Repetir click derecho","Repetir click izquierdo"])
time.sleep(5)
a = minecraft(action)