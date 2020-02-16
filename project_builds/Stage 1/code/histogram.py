import numpy as np
import cv2
import os 
import matplotlib.pyplot as plt

"""
Created on Sat Feb 15 14:49:04 2020

@author: ealegre
"""

def histogram(I):
    
    # Flattens the input image into a 1D list 
    img = I.flatten().tolist()
    
    # Get number of pixels in image
    pxl_count = len(img)
    
    # Generates an empty integer list of range 0 to 256
    hist = list(map(int, np.zeros(256)))
    
    levels = range(len(hist))
    
    # Loops through flattened image to find the intensity cound for each level
    for i in img:
        hist[i] = hist[i] + 1
    
    
    # Display OG image with histogram
    plt.figure(figsize=(20,20))
    
    plt.subplot(212)
    plt.bar(levels, hist, width=1, zorder=2)
    plt.title('Histogram of Image')
    plt.xlabel('Grey Level')
    plt.grid(True)
    
    plt.subplot(211)
    plt.tick_params(axis='both', which='both', top=False, bottom=False)
    plt.imshow(I, cmap='gray')
    plt.title('Input Image')
    
    return hist