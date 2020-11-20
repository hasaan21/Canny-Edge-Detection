from Gaussian_filter import gaussian_filter
from Sobel_filter import sobel_filter
from Non_max_supression import supression
from Thresholding import double_threshold

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('canny_practice.png',0)

cv2.imshow('Original Image',image)

#Step-1: Noise Reduction

blurred_image = gaussian_filter(image,3,1)

cv2.imshow('Blurred Image',blurred_image)

#Step-2: Gradient Calculations

filtered_image, theta = sobel_filter(blurred_image)
cv2.imshow('Filtered Image',filtered_image)

#Step-3: Non Maximum Supression

supressed_image = supression(filtered_image,theta)
cv2.imshow('Supressed Image',supressed_image)

#Step-4+5: Double Thresholding and Hysteresis 

threshed_image = double_threshold(supressed_image)
#cv2.imwrite('canny_output.png',threshed_image)
cv2.imshow('Thresholded Image',threshed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()