import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space

### --- COMPLETE --- ###

def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    -----------
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    # --- FILL ME IN ---
    # Initialize the required number of points
    num_of_points = 4

    # Initialize the A Matrix as a blank, we will be appending the contents below
    A_init = []

    # Screen the input points to extract the corresponding 4 points required to create the A matrix
    for i in range(num_of_points):
        x, y = I1pts[0][i], I1pts[1][i]
        u, v = I2pts[0][i], I2pts[1][i]
        # Using Eq 2.4 from Dubrofsky's MASc Thesis, find the corresponding A_i matrix
        A_i = np.array(((-x, -y, -1, 0, 0, 0, u*x, u*y, u), (0, 0, 0, -x, -y, -1, v*x, v*y, v)))
        # Append the matrix to our original A_list matrix
        A_init.append(A_i)
    A = np.concatenate(A_init)

    # We know that the solution for H is the 1D null space of A, so we use that to find out H matrix
    H = null_space(A)

    # According to Hartley and Zisserman, the result of the DLT is dependent on the origin and scale of the image's
    # coordinate system. Thus a normalization step is needed to ensure the solution converges to the right result
    H = H/H[8]

    # Reshape back to a 3x3 matrix
    H = np.reshape(H, (3,3))


    # ------------------

    return H, A


if __name__ == '__main__':
    print('hello')
