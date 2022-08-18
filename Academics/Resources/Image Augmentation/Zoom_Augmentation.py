# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:05:52 2019

@author: User
"""

# example of zoom image augmentation
from numpy import expand_dims
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot

from scipy import ndimage, misc
import numpy as np
import cv2, os
import numpy as np

def cacao(source,destination):
    count = 0
    for fn in os.listdir(source):
        # load the image
        img = cv2.imread(source+"//"+fn)
        # convert to numpy array
        data = img_to_array(img)
        # expand dimension to one sample
        samples = expand_dims(data, 0)
        
        datagenZoom = ImageDataGenerator(zoom_range=[.5,.7])
        datagenBright = ImageDataGenerator(brightness_range=[1.1,1.5])
        datagenHor = ImageDataGenerator(width_shift_range=[-200,200])
        datagenVer = ImageDataGenerator(height_shift_range=[-200,200])
        datagenRot = ImageDataGenerator(rotation_range=90)
        
        # prepare iterator
        itZ = datagenZoom.flow(samples, batch_size=1)
        itB = datagenBright.flow(samples, batch_size=1)
        itH = datagenHor.flow(samples, batch_size=1)
        itV = datagenVer.flow(samples, batch_size=1)
        itR = datagenRot.flow(samples, batch_size=1)
        
        # generate batch of images
        batchZ = itZ.next()
        batchB = itB.next()
        batchH = itH.next()
        batchV = itV.next()
        batchR = itR.next()
            # convert to unsigned integers for viewing
        imageZ = batchZ[0].astype('uint8')
        imageB = batchB[0].astype('uint8')
        imageH = batchH[0].astype('uint8')
        imageV = batchV[0].astype('uint8')
        imageR = batchR[0].astype('uint8')
            
        cv2.imwrite(destination+"//Zoom"+str(count)+".jpg", imageZ)
        cv2.imwrite(destination+"//Brightness"+str(count)+".jpg", imageB)
        cv2.imwrite(destination+"//Hor"+str(count)+".jpg", imageH)
        cv2.imwrite(destination+"//Ver"+str(count)+".jpg", imageV)
        cv2.imwrite(destination+"//Rotate"+str(count)+".jpg", imageR)
        count+=1
#cacao("A", "Augmented Images")
cacao("D:\\Images\\train\\UNKNOWN VARIETY", "D:\\Images\\Cacao\\train\\UNKNOWN VARIETY")

