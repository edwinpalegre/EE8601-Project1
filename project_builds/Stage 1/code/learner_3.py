# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:49:47 2020

@author: ealegre
"""

import matplotlib.pyplot as plt
from histogram_eq import histogram_eq
import os
import cv2 
from histogram import histogram

os.chdir(r'C:\Users\ealegre\Documents\Academics\Ryerson University - MASc\Courses\EE8601 - Fundamentals of Computer Vision and Deep Learning\Project 1 - Billboard Hacking\project_builds\Stage 1')


I = cv2.imread("./pictures/uoft_soldiers_tower_dark.png", 0)
J = histogram_eq(I)

plt.figure()
plt.imshow(I, cmap = "gray", vmin = 0, vmax = 255)
plt.figure()
plt.imshow(J, cmap = "gray", vmin = 0, vmax = 255)