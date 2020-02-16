import numpy as np
from numpy.linalg import inv

def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    4 pixels to compute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    #--- FILL ME IN ---

    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')
        
    # Bilinear Interpolation Info
    # http://supercomputingblog.com/graphics/coding-bilinear-interpolation/
        
        
    # Grab the x and y from input point pt
    x = pt[0, 0]
    y = pt[1, 0]
    
    # Find the 4 NN
    x2_ = np.floor(x).astype(int) + 1
    x1_ = np.ceil(x).astype(int) - 1
    y2_ = np.floor(y).astype(int) + 1
    y1_ = np.ceil(y).astype(int) - 1
    
    # Restrict the range of your points to avoid an index out of range error
    x1 = np.clip(x1_, 0, I.shape[1] - 1)
    x2 = np.clip(x2_, 0, I.shape[1] - 1)
    y1 = np.clip(y1_, 0, I.shape[0] - 1)
    y2 = np.clip(y2_, 0, I.shape[0] - 1)
    
    # Find the corresponding pixel intensity to the image, I.
    Q11 = I[y1, x1]
    #print('Q11 =', Q11)
    Q12 = I[y2, x1]
    #print('Q12 =', Q12)
    Q21 = I[y1, x1]
    #print('Q21 =', Q21)
    Q22 = I[y2, x2]
    #print('Q22 =', Q22)
    
    
    
    # Calculate R1, weighted average of Q11 and Q21
    R1 = ((x2 - x)/(x2 - x1))*Q11 + ((x - x1)/(x2 - x1))*Q21
    #print('R1 =', R1)
    
    # Calculate R2, weighted average of Q12 and Q22
    R2 = ((x2 - x)/(x2 - x1))*Q12 + ((x - x1)/(x2 - x1))*Q22
    #print('R2 =', R2)
    
    # Calculate P, weighted average of R1 and R2
    b = ((y2 - y)/(y2 - y1))*R1 + ((y - y1)/(y2 - y1))*R2
    
    #------------------

    return np.round(b)

