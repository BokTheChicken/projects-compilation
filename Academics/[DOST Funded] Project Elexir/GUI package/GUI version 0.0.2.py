# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:07:32 2019

@author: K.Sibunga
"""

# import system module
import sys
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


# import Opencv module
from GUI2 import *
import cv2
from imageai.Prediction.Custom import CustomImagePrediction
import os
import cv2
from cv2 import *
import numpy as np
import time, os

execution_path = os.getcwd()
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "model_ex-012_acc-0.980136.h5"))
prediction.setJsonPath(os.path.join(execution_path, "Variety (2).json"))
prediction.loadModel(num_objects=4)


class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.pushButton.clicked.connect(self.Close)
    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 491)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
            # start timer
            self.timer.start(0)
            # update control_bt text
            self.ui.control_bt.setText("Identify")
            # if timer is started
        else:
            ret, image = self.cap.read()
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imwrite("test.jpg", image)
            varietyArray = prediction.predictImage("test.jpg")
            variety = varietyArray[0][0]
            print(variety)
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Capture")
            self.ui.label.setText(str(variety))
    def Close(self):    
        self.ui.pushButton.clicked.connect(self.close)   
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())