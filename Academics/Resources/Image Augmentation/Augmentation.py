# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:25:33 2019

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

        
gen = ImageDataGenerator(rotation_range = 10, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.15, zoom_range=0.1, channel_shift_range=10.,horizontal_flip=True)

image_path = "C:\\Users\\User\\Desktop\\Training Program\\Data Augmentation\\180Degrees_48.jpg"

image = np.expand_dims(plt.imread(image_path),0)
plt.imshow(image[0])

aug_iter = gen.flow(image, save_to_dir = "C:\\Users\\User\\Desktop\\Training Program\\Data Augmentation\\Augmented Images", save_format='jpg' ) #gen.flow_from_directory()
aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]




