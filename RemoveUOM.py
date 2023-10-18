import pyautogui
import time

time.sleep(3)

test = pyautogui.locateCenterOnScreen('rightarrow.png')

testx = test[0]
testy = test[1]

pyautogui.click(testx,testy)