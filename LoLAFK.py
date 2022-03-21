import pyautogui
import time
import keyboard
import os
from art import *

pyautogui.alert("MADE BY FARES")
def stop():
    pyautogui.alert("AFK STOP")
    os._exit(0)
keyboard.add_hotkey('ctrl+shift+a', stop)

#Keybinds
tprint("MADE_BY_(FARES)")
aprint("happy")
if keyboard.read_key() == "k": #FUNKAR INTE PÅ LoL starta innan spelet
	#Rörelse
	while True:
		time.sleep(5)
		pyautogui.doubleClick(button='right',x=1349,y=390)
		time.sleep(5)
		pyautogui.doubleClick(button='right',x=861,y=358)
		time.sleep(5)
		pyautogui.doubleClick(button='right',x=780,y=663,)