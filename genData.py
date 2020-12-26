import numpy as np 
from pyautogui import screenshot
from cv2 import cvtColor, COLOR_RGB2BGR, imwrite
import keyboard,json
from time import sleep

def take(obj, c):
    obj['counter']+=1
    print(obj['counter'])
    img = (np.array(screenshot()))[820:1020,650:850]
    img = cvtColor(img,COLOR_RGB2BGR)
    imwrite("./data/{}/image_{}.png".format(c,obj['counter']), img)


with open('info.json','r') as file:
    obj = json.load(file)
print(obj)
start  = False
while True:
    if start:
        sleep(0.01)
        take(obj,"0")
    
    if keyboard.is_pressed('space'):
        start = True
        #take(obj,"1")
        #keyboard.write('q', delay=0)

    elif keyboard.is_pressed('p'):
        start = False

    elif keyboard.is_pressed('tab'):
        print(obj)
        with open('info.json','w') as file:
            json.dump(obj, file)
        break

