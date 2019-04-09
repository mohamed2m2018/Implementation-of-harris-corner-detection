import cv2
import numpy as np
from scipy import signal


# Calculating gradient at X direction


def calculateIx(grey_image):
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return signal.convolve2d(grey_image,kernel,mode='same')


# Calculating gradient at Y direction

 
def CaculateIy(grey_image):
    #transpose of the Ix kernel 
    kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    return signal.convolve2d(grey_image,kernel,mode='same')   


#Reading The image
image = cv2.imread("box.jpg", 1)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
     

#Calculating Ix,Iy,Ixx,Iyy,Ixy
Ix=calculateIx(gray_image)
Iy=CaculateIy(gray_image)
Ixx = pow(Ix,2)
Iyy = pow(Iy,2)
Ixy = Ix*Iy
