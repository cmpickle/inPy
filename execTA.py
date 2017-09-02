import pyautogui
import os
import time

os.system("TASKKILL /F /IM iexplore.exe")

pyautogui.moveTo(800, 1180)
pyautogui.click()
pyautogui.moveTo(100,30)
pyautogui.click()
pyautogui.moveTo(100, 50)
pyautogui.click()
pyautogui.moveTo(1125, 925)
pyautogui.click()