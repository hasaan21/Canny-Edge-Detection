import numpy as np

def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2 
    x, y = np.mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * np.pi * np.square(sigma)) * np.exp(-(np.square(x) + np.square(y)) / (2 * np.square(sigma)))
    return g


def gaussian_filter(image, k_size, sigma):
    height, width = image.shape

    # dst image height and width
    dst_height = height - k_size + 1
    dst_width = width - k_size + 1

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = np.zeros((dst_height * dst_width, k_size * k_size))
    row = 0
    for i in range(0, dst_height):
        for j in range(0, dst_width):
            window = np.ravel(image[i : i + k_size, j : j + k_size])
            image_array[row, :] = window
            row += 1
   
    #  turn the kernel into shape(k*k, 1)
    gaussian_kernel = gen_gaussian_kernel(k_size, sigma)
    filter_array = np.ravel(gaussian_kernel)

    # reshape and get the dst image
    dst = np.dot(image_array, filter_array).reshape(dst_height, dst_width).astype(np.uint8)
    
    return dst