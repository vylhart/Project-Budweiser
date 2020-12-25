import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf
import numpy as np 
from pyautogui import screenshot, press, click
from cv2 import cvtColor, COLOR_RGB2BGR
import keyboard
from time import sleep
from datetime import datetime
model = tf.keras.models.load_model('./hdf5/model.h5')

def take():
    img = (np.array(screenshot()))[750:,1200:1500]
    img = cvtColor(img,COLOR_RGB2BGR)
    return img

def predict(model, img):
    img = keras.preprocessing.image.smart_resize(img, (180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    return predictions[0][0]

started = False
print('***Ready***')
try:
    while True:
            if keyboard.is_pressed('s'):
                started = True
                print('***started***')
            elif keyboard.is_pressed('e'):
                print('***over***')
                started = False
                break
            elif keyboard.is_pressed('p'):
                print('***Paused***')
                started = False
            elif started:
                sleep(0.05)
                t1 = datetime.now()
                img = take()
                score = predict(model,img)
                if score>0.99:
                    #press("space")
                    click(x=700,y=900)
                    t2 = datetime.now()
                    t = t2-t1
                    print('Jumping....', t.microseconds)
except KeyboardInterrupt:
    print('Keyboard Interrupt')
