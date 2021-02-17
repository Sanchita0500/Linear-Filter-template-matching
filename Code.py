import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from PIL import Image
%matplotlib inline

# Implement Linear Filtering technique on an image using a linear filter #correlation
def linear_filter(image, filter_): # 'filter' is a keyword in python, so is the underscore at the end.
    """
    Performs linear filtering on an image.
    Assume image size is W1xW2, filter size is F1xF2.
    
    Arguments:
    image -- input image possibly with 3 channels(RGB).
    filter_ -- linear filter to apply on image.
    
    Returns:
    result -- filtered image. 
    """
    # DO NOT CHAGE THIS CODE    
    image = np.array(image.convert('L')) # converts image to gray scale, so that it is easy to apply filter
    image_height, image_width = image.shape[0], image.shape[1]

    filter_ = np.array(filter_.convert('L'))
    filter_height, filter_width = filter_.shape[0], filter_.shape[1]

    # result shape will be of size --> (((W1−F1+2P) / S) + 1) x (((W2−F2+2P) / S) + 1), where 'P' is padding length
    # S is stride length.For now we will use simplest setting P=0,S=1. See the next line.

    result_height, result_width = (image_height - filter_height) + 1, (image_width - filter_width) + 1
    result = np.array([[0 for j in range(result_width)] for i in range(result_height)])
    
    ssd_min=sys.maxsize
    for i in range(0,result_height):
        for j in range(0,result_width):
            ssd=np.mean(np.square(np.subtract(image[i:i+filter_height,j:j+filter_width],filter_)))
            if(ssd<ssd_min):
                x1,y1=j,i
                x2,y2=x1+filter_width,y1+filter_height
                ssd_min=ssd
    
    result=cv2.rectangle(image, (x1, y1), (x2, y2), (255,0,0), 2)
    return result

# To test your implementation, run the below code.
image = Image.open('..\\hills.jpeg')
filter_ = Image.open('..\\template.png')
result = linear_filter(image, filter_)

plt.imshow(result,cmap="gray")
plt.title('Filtered Image')
plt.show()
