# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite
from matplotlib import pyplot as plt

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq
import os
import cv2

os.chdir(r'C:\Users\ealegre\Documents\Academics\Ryerson University - MASc\Courses\EE8601 - Fundamentals of Computer Vision and Deep Learning\Project 1 - Billboard Hacking\project_builds\Stage 1\code')

def billboard_hack():
    """
    Hack and replace the billboard!
    Parameters:
    ----------- 
    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    
    
    # Bounding box in Y & D Square image.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    Iyd = imread(r'./pictures/yonge_dundas_square.jpg')
    Ist = imread(r'./pictures/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---

    # Let's do the histogram equalization first.
    Ist_histeq = histogram_eq(Ist)

    # Compute the perspective homography we need...
    H, A = dlt_homography(Iyd_pts, Ist_pts)
    
    # Define the path of interest (polygon)
    '''
    Path represents a series of possibly disconnected, possibly closed, line and curve segments.
    
    The underlying storage is made up of two parallel numpy arrays:
    vertices: an Nx2 float array of vertices
    codes: an N-length uint8 array of vertex types
    
    '''
    vertices = np.array([[x,y] for x,y in zip(Iyd_pts[0], Iyd_pts[1])])
    polygon = Path(vertices)
    
    # Find hwight and width of the YD picture
    height, width, _ = Iyd.shape
    
    # Iterate through 
    for x in range(width):
        for y in range(height):
            # uses matplot.lib.paths.contains_points() to verify if the current point is in the path (polygon)
            if polygon.contains_points([[x, y]]):
                # If 'True', then the dot product of the perpective homography matrix, H, and the current normalized            
                # coordinates, [x ,y, 1]. This is the new homogeneous coordinate
                p = H.dot(np.array([x, y, 1]))
                # The resultant p coordinate is then normalized to by dividing the 3rd coordinate, thereby giving us the new x 
                # and y
                xp, yp, _ = p / p[2]
                # Generate a 2x1 array for the point to comply with the input requirement for bilinear interp
                pt = np.array([[xp], [yp]])
                # Since the new transform warps and resizes the ST picture, it must be resized after its new perspectice 
                # coordinates have been found. Use bilinear interpolation for this
                interp = bilinear_interp(Ist, pt)
                # Write the new intensity value for the YD pic. Note that a 3 element array is needed because the YD picture 
                # is in RGB
                Ihack[y, x] = np.array([interp, interp, interp])    
                
    #-----------------
    
    imwrite('billboard_hacked.png', Ihack)
    while(True):
        cv2.imshow('Hacked Billboard', Ihack)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
        
        
    return Ihack

if __name__ == '__main__':
    hack = billboard_hack()
