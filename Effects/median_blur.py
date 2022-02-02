import cv2
import numpy 

def get_kernel_median(img,row_initial,col_initial,kernel_size):
    values = []
    for row in range(row_initial,row_initial+kernel_size):
        for col in range(col_initial,col_initial+kernel_size):
            values.append(img[row,col])
    values.sort()
    median = values[len(values)//2]
    return median 

def set_kernel_values(img,row_initial,col_initial,kernel_size,value):
   img[row_initial+kernel_size//2,col_initial+kernel_size//2] = value 

def median_blur(img, kernel_size):
    blurred_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    for row in range(0,len(blurred_img)-kernel_size):
        for col in range(0,len(blurred_img[0])-kernel_size):
            median = get_kernel_median(blurred_img,row,col,kernel_size)
            set_kernel_values(blurred_img,row,col,kernel_size,median)
    
    blurred_img = cv2.cvtColor(blurred_img,cv2.COLOR_GRAY2RGB)
    return blurred_img

