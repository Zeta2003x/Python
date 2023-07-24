import pyautogui
import pyperclip
import time

texto = """arquitectura de computadoras"""

def pegar(pp):
	pyperclip.copy(pp)
	pyautogui.keyDown("ctrl")
	pyautogui.press("v")
	pyautogui.keyUp("ctrl")
	pyautogui.press("tab")
	time.sleep(0.2)

for i in texto:
	a = bin(ord(i))[2:].zfill(8)
	if i == "\n": i = "Nueva línea"
	elif i == " ": i= "Espacio"
	print(f"{i} = {a}".format())

