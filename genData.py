import numpy as np 
from pyautogui import screenshot
import cv2
from cv2 import cvtColor, COLOR_RGB2BGR, imwrite
import keyboard,json
from time import sleep

def take(obj, c):
    obj['counter']+=1
    print(obj['counter'])
    img = (np.array(screenshot()))[750:,600:1200]
    img = cvtColor(img,cv2.COLOR_RGB2BGR)
    imwrite("./data/{}/image_{}.png".format(c,obj['counter']), img)


with open('info.json','r') as file:
    obj = json.load(file)
print(obj)

while True:
    if keyboard.is_pressed('space'):
        take(obj,"1")
        sleep(0.75)
        take(obj,"0")
        #keyboard.write('q', delay=0)

    elif keyboard.is_pressed('tab'):
        print(obj)
        with open('info.json','w') as file:
            json.dump(obj, file)
        break

