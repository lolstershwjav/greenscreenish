import cv2
import time
import numpy as np

camera = cv2.VideoCapture(0)

camera.set(3 , 640)
camera.set(4 , 480)

bgImg = cv2.imread("bgImg.jpeg")

bgImg = cv2.resize(bgImg(640, 480))

#Starting the webcam    








#Reading the captured frame until the camera is open
while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([])
        upper_bound = np.array([])

        # thresholding image
        mask  = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # inverting the mask
        mask = cv2.bitwise_not(mask)
        
        # bitwise and operation to extract foreground / person
        person = cv2.bitwise_and(frame, frame , mask=mask)
        # final image

        finalImg = np.where(person == 0, bgImg, person)

        # show it
        cv2.imshow('frame' , finalImg)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()