import os
from cv2 import imwrite
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow import keras
import tensorflow as tf
import numpy as np 
from pyautogui import screenshot,click
import keyboard
from time import sleep
#from datetime import datetime
model = tf.keras.models.load_model('./hdf5/model2.h5')
c = 36
def predict():
    global c
    img = (np.array(screenshot()))[820:1020,1400:1600]
    img_array = tf.expand_dims(img, 0)
    predictions = (model.predict(img_array))[0][0]
    score = 1 if predictions > 0.5 else 0
    if score:
        c+=1
        imwrite("./data/1/image_{}.png".format(c), img)
    

    return score

started = False
print('***Ready***')
try:
    while True:
            if started:
                #sleep(0.01)
                #t1 = datetime.now()
                score = predict()
                if score:
                    click(x=1000,y=1060)
                    #t2 = datetime.now()
                    #t = t2-t1
                    #print(t.microseconds)
            elif keyboard.is_pressed('space'):
                started = True
                print('***started***')

            if keyboard.is_pressed('tab'):
                print('***over***')
                started = False
                break
            elif keyboard.is_pressed('p'):
                print('***Paused***')
                started = False
            
except KeyboardInterrupt:
    print('Keyboard Interrupt')
