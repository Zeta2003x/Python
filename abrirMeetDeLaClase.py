import time
import pyautogui
from datetime import datetime

def openMeet():
	pyautogui.hotkey("win","2")
	time.sleep(3)
	pyautogui.hotkey("win","up")
	time.sleep(0.5)
	pyautogui.hotkey("ctrl","t")
	time.sleep(0.5)
	pyautogui.write("{}\n".format(link), interval=0.02)
	time.sleep(2.5)
	pyautogui.moveTo(620, 800, 1)
	time.sleep(0.5)
	pyautogui.click()
	time.sleep(0.5)
	pyautogui.moveTo(720, 800, 0.2)
	time.sleep(0.5)
	pyautogui.click()

def main():
	global link
	day = datetime.today().weekday()
	if day == 1: link = "https://meet.google.com/cys-wmak-bkb?pli=1&authuser=1"
	elif day == 3: link = "https://meet.google.com/iby-iteh-pry?pli=1&authuser=1"
	elif day == 4: link = "https://meet.google.com/huc-poox-ros?pli=1&authuser=1"
	openMeet()

if __name__ == '__main__':
	main()