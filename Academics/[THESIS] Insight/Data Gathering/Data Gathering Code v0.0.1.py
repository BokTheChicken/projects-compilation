# -*- coding: utf-8 -*-
"""
@author: K.Sibunga
"""
import shutil,cv2,numpy as np,os
import time
import threading
    
def show_webcam(mirror=False,VidName = 'video.mp4',t=5):    
    cam = cv2.VideoCapture(0)
    width = int(cam.get(3))
    height = int(cam.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(VidName,fourcc,10.0,(width,height))
    start = time.time()
    while True: #Ayusin ang timer
        ret_val, img = cam.read()
        stop = time.time()
        if mirror:
            img = cv2.flip(img, 1)
            
        if cv2.waitKey(1) == 27:
            break
        if t <= stop-start:
            break
        
        out.write(img)
        cv2.imshow('Camera',img)
            
    cam.release()
    out.release()
    cv2.destroyAllWindows()

    
def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)
    cap = cv2.VideoCapture(pathIn)
    count=0
    while(cap.isOpened()):
        ret, frame= cap.read()
        if ret == True:
            print('Read %d frame: ' %count,ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)),frame)
            count +=1
        else:
            break
        
    cap.release()
    cv2.destroyAllWindows()

        
def main():
    user='0'
    test=os.path.exists('%s' %user)

    while test == True:
        user= str(int(user)+1)
        test=os.path.exists('%s' %user)

    os.mkdir(user)
    os.chdir(user)
    path = os.getcwd()
             
    show_webcam(mirror=True,VidName='RoomLight.mp4',t=5)
    show_webcam(mirror=True,VidName='Dark.mp4',t=15)
    show_webcam(mirror=True,VidName='Direct.mp4',t=20)
    
    source1 = 'RoomLight.mp4'
    destination1 = path+'\\Room Light'
    extractFrames('RoomLight.mp4',destination1)
    shutil.move(source1,destination1)
    
    source2 = 'Dark.mp4'
    destination2 = path+'\\Dark'
    extractFrames('Dark.mp4',destination2)
    shutil.move(source2,destination2)
    
    source3 = 'Direct.mp4'
    destination3 = path+'\\Direct Light'
    extractFrames('Direct.mp4',destination3)
    shutil.move(source3,destination3)    
    


if __name__== '__main__':
    main()
