import numpy as np
import cv2

def im2col(image, block_size):
    height, width = image.shape
    dst_height = height - block_size[1] + 1
    dst_width = width - block_size[0] + 1
    image_array = np.zeros((dst_height * dst_width, block_size[1] * block_size[0]))
    row = 0
    for i in range(0, dst_height):
        for j in range(0, dst_width):
            window = np.ravel(image[i : i + block_size[0], j : j + block_size[1]])                    
            image_array[row, :] = window
            row += 1        
    return image_array


def img_convolve(image, filter_kernel):
    height, width = image.shape
    k_size = filter_kernel.shape[0]
    pad_size = k_size // 2

    # Pads image with the edge values of array.
    image_tmp = np.pad(image, pad_size, mode="constant",constant_values=(0))

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = im2col(image_tmp, (k_size, k_size))

    #  turn the kernel into shape(k*k, 1)
    kernel_array = np.ravel(filter_kernel)

    # reshape and get the dst image
    dst = np.dot(image_array, kernel_array).reshape(height, width)
    return dst

def classify_angle(theta):
    height, width = theta.shape

    for i in range(0, height):		
        for j in range(0, width):	

            theta[i, j] = theta[i, j]*180/np.pi # transform theta into degree

            if theta[i, j]<0: # tranform which degree < 0 to 0-360
                theta[i, j] = theta[i, j]+360 # if degree is negative +360 to become positive degree
            
    		# classify every pixel
            if (theta[i, j]<22.5 and theta[i, j]>=0) or (theta[i, j]>=157.5 and theta[i, j]<202.5) or (theta[i, j]>=337.5 and theta[i, j]<=360):
                   theta[i, j]=0 
            elif (theta[i, j]>=22.5 and theta[i, j]<67.5) or (theta[i, j]>=202.5 and theta[i, j]<247.5):
                   theta[i, j]=45 
            elif (theta[i, j]>=67.5 and theta[i, j]<112.5)or (theta[i, j]>=247.5 and theta[i, j]<292.5):
                   theta[i, j]=90 
            else:
                   theta[i, j]=135 

    #theta = theta.astype(np.uint8)
    return theta

def sobel_filter(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    dst_x = np.abs(img_convolve(image, kernel_x))
    dst_y = np.abs(img_convolve(image, kernel_y))
   
    # modify the pix within [0, 255]
    dst_x = dst_x * 255 / np.max(dst_x)
    dst_y = dst_y * 255 / np.max(dst_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))

    #normalize
    dst_xy = dst_xy * 255 / np.max(dst_xy)
    dst = dst_xy.astype(np.uint8)

    theta = np.arctan2(dst_y, dst_x)
    theta = classify_angle(theta)
    
    return dst, theta    