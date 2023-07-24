import time
import pyautogui

tiempo = pyautogui.prompt(text="Tiempo (en minutos) hasta suspender la computadora",title="Tiempo")
time.sleep(float(tiempo)*60)
pyautogui.keyDown("win")
pyautogui.press("x")
pyautogui.keyUp("win")
time.sleep(1)
pyautogui.press("u")
time.sleep(1)
pyautogui.press("s")