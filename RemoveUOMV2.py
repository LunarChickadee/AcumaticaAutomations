import pyautogui
import time

time.sleep(2)

for y in range(600):
    #arrowclick
    time.sleep(0.2)
    pyautogui.click(562,228)

    #xclick
    for x in range(25):
        time.sleep(.7)
        pyautogui.click(1090,500)
    #22 to delete

    #savebuttonclick
    time.sleep(0.2)
    pyautogui.click(238,228)
    time.sleep(0.2)
    pyautogui.click(238,228)
    time.sleep(1)
