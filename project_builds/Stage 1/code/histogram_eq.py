import numpy as np
import cv2
import os 
import matplotlib.pyplot as plt
from histogram import histogram

def histogram_eq(I):
    """
    Histogram equalization for greyscale image.
    Perform histogram equalization on the 8-bit greyscale intensity image I
    to produce a contrast-enhanced image J. Full details of the algorithm are
    provided in the Szeliski text.
    Parameters:
    -----------
    I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    Returns:
    --------
    J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
    """
    #--- FILL ME IN ---

    # Verify I is grayscale.
    if I.dtype != np.uint8:
        raise ValueError('Incorrect image format!')
    
    # Read image
    img = I
    [i, j] =[img.shape[0], img.shape[1]]
    
    # Find histogram
    hist_array = list(map(float, histogram(I)))
    
    # Find pixel count
    pxl_count = len(img.flatten())
    
    '''
    --- Histogram Equalization ---
    
    Steps for Histogram Equalization
            
    1. Calculate Probability Mass Function (PMF) -  pmf(greyLevels+1) = hist_array(greyLevels+1)/(i*j)
    
    2. Calculate Cumulative Distribution Function (CDF) - cdf(greyLevels+1) = cdf(greyLevels+1) + prev_sum
    
    3. Multiply the CDF by the number of grey levels minus 1, divided by the 
    area of the image - (greyLevels-1/(i*j))
    
    4. Round that result
    
    ------------------
    '''
    
    prev_sum = 0
    
    # Step 1
    pmf = [x / pxl_count for x in hist_array]
    cdf = np.zeros(len(pmf))
    
    # Step 2 and 3
    for x in range(len(pmf)):
        cdf[x] = pmf[x] + prev_sum
        prev_sum = cdf[x]
    
    # Step 4
    hist_equal = [round(x*255).astype(int) for x in cdf]     
    
    img2 = np.zeros([i,j]).astype(int)
        
    # Assign new mapping based off the histogram equalization
    for row in range(0, i):
        for col in range(0, j):
            img2[row, col] = hist_equal[img[row, col]]
    
    plt.figure(2)
    histogram(img2)

    return img2