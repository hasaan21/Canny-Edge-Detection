import numpy as np

def double_threshold(image):
    highThresholdRatio = 0.15
    lowThresholdRatio = 0.1

    height, width = image.shape
    highThreshold = image.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if image[i,j] > highThreshold:
                image[i,j] = 255
            elif image[i,j] < lowThreshold:
                image[i,j] = 0
            else:
                #Step-6: pixels in mid range
                if((image[i-1,j-1] > highThreshold) or 
                (image[i-1,j] > highThreshold) or
                (image[i-1,j+1] > highThreshold) or
                (image[i,j-1] > highThreshold) or
                (image[i,j+1] > highThreshold) or
                (image[i+1,j-1] > highThreshold) or
                (image[i+1,j] > highThreshold) or
                (image[i+1,j+1] > highThreshold)):
                    image[i,j] = 255                
    return image                    

