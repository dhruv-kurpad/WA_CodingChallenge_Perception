import cv2
import numpy as np
#This file was used to find the low and high bounds for my cone mask
#Would click on cones in red.png and print hsv values
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_value = hsv[y, x]
        print(hsv_value)

image = cv2.imread('red.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('Image', image)
cv2.setMouseCallback('Image', pick_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
