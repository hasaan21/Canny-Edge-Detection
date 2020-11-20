import numpy as np

def supression(magnitude, theta):
    height, width = magnitude.shape

    for i in range(1, height-1):		
        for j in range(1, width-1): 
            if theta[i,j]==0:
                if (magnitude[i, j]<=magnitude[i, j+1]) or (magnitude[i, j]<=magnitude[i, j-1]): 
                    magnitude[i][j]=0 
            elif theta[i, j]==45: 
                if (magnitude[i, j]<=magnitude[i-1, j+1]) or (magnitude[i, j]<=magnitude[i+1, j-1]): 
                    magnitude[i, j]=0 
            elif theta[i, j]==90: 
                if (magnitude[i, j]<=magnitude[i+1, j]) or (magnitude[i, j]<=magnitude[i-1, j]): 
                    magnitude[i, j]=0 
            else: 
                if (magnitude[i, j]<=magnitude[i+1, j+1]) or (magnitude[i, j]<=magnitude[i-1, j-1]): 
                    magnitude[i, j]=0 

    return magnitude