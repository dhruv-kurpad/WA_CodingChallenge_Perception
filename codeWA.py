import cv2
import numpy as np

#Image with cones
image = cv2.imread('red.png')
#Convert to hsv to make look for cones by color
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Test vals (exit signs?)
#Cones
#178, 232, 169
#175, 255, 224

#Sign
#154, 48, 255

#I used these to define a range of color values that a cone would fall in
#ignore the exit signs
lowCone = np.array([165, 200, 160])
highCone = np.array([190, 270, 240])

# Mask for colors within low and high cone range
mask = cv2.inRange(hsv, lowCone, highCone)

# Find values that match the mask
cones, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
left_points = []
right_points = []

for cone in cones:
    #Simplify problem by making cone a box
    x, y, w, h = cv2.boundingRect(cone)
    
    #Cones on the left side
    if x < image.shape[1] // 2:
        left_points.append((x + w // 2, y + h))
    #Cones on the right side
    else:
        right_points.append((x + w // 2, y + h))

left_points = np.array(left_points)
right_points = np.array(right_points)

# Points made, Draw lines
#y = mx+b
left_line = np.polyfit(left_points[:, 0], left_points[:, 1], 1)
left_m, left_b = left_line

right_line = np.polyfit(right_points[:, 0], right_points[:, 1], 1)
right_m, right_b = right_line

# Make a line with 2 points (top and bottom) so it's straight and continuous
height = image.shape[0]
left_start = (0, int(left_b))
left_end = (image.shape[1] // 2, int(left_m * (image.shape[1] // 2) + left_b))

right_start = (image.shape[1], int(right_m * image.shape[1] + right_b))
right_end = (image.shape[1] // 2, int(right_m * (image.shape[1] // 2) + right_b))

# Draw
cv2.line(image, left_start, left_end, (0, 0, 255), 5)
cv2.line(image, right_start, right_end, (0, 0, 255), 5)

# Save answer
cv2.imwrite('answer.png', image)

#delete
cv2.imshow('answer', image)
cv2.waitKey(0)
cv2.destroyAllWindows()