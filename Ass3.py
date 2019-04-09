import cv2
import numpy as np
from scipy import signal


# Calculating gradient at X direction


def Ix(grey_image):
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return signal.convolve2d(grey_image,kernel,mode='same')

 
def Iy(grey_image):
    #transpose of the Ix kernel 
    kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    return signal.convolve2d(grey_image,kernel,mode='same')   
