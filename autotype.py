import time
import pyautogui
import keyboard
time.sleep(5)
def mimic_typing(text, typing_speed=0.05):
    position = 0  # start position
    while position < len(text):
        if keyboard.is_pressed('['):  # if key 'q' is pressed 
            print('Paused. Press "]" to resume.')
            while True:  # wait for 'r' to be pressed
                if keyboard.is_pressed(']'):  
                    print('Resumed.')
                    break
                time.sleep(0.03)
        pyautogui.typewrite(text[position])
        position += 1
        time.sleep(typing_speed)

text = ""
mimic_typing(text)
