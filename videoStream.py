import numpy as np
import cv2
import argparse

#Working at 720p resolution
#1080p resolution does not function except for the initial frame
#TODO: I believe capping FPS will solve issue as mobius cam can only support 30fps at 1080p
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
#ap = argparse.ArgumentParser()
#ap.add_argument(',-i', '--image', help = 'path to image')
#args = vars(ap.parse_args())
boundaries = [([85,85,252], [1,1,160])]
while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite('lastFrame.jpg', frame)
    #Single Frame Operations Here
    newFrame = cv2.imread('lastFrame.jpg')
    if(ret):
        for(lower, upper) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            mask = cv2.inRange(newFrame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask = mask)

        #Display the finished frame
        cv2.imshow('frame', output)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
#Release capture when finished
cv2.imwrite('lastFrame.jpg',gray)
cap.release()
cv2.destroyAllWindows()