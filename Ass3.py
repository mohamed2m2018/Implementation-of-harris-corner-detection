import cv2
import numpy as np
from scipy import signal


#Using sobel filter to calculate derivatives 

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


offset = 2
k = 0.08

imageHeight, imageWidth = gray_image.shape

#initializing Harris Response Array

HarrisResponse = np.zeros((width - offset, height-offset))

#constructing Harris response array

for y in range(offset, height-offset):
    for x in range(offset, width - offset):
        Sxx = float np.sum(Ixx[y-offset:y+1+offset, x-offset:x+1+offset])

        Syy = float np.sum(Iyy[y-offset:y+1+offset, x-offset:x+1+offset])

        Sxy = np.sum(Ixy[y-offset:y+1+offset, x-offset:x+1+offset])

        determinant = (Sxx * Syy) - (Sxy ** 2)

        trace = Sxx + Syy

        HarrisResponse[y][x] = determinant - k * (trace ** 2)





