# WA_CodingChallenge_Perception
##answer.png

## Methodolgy
### Objective:
Create a perception algorithm that can detect the boundaries of a straight path defined by cones taken by a camera attached to a vehicle. 

Inputs  | Outputs
------- | -------
png file | same png file with path

### Steps:
1) Define range of values for cone
2) Convert image to HSV
3) Search image for cones
4) Record location of cones
5) Create an equation y = mx+b for locations
6) Draw line on original image
7) Save result as answer.png

## What did you try and why do you think it did not work.
I tried to look for cones based on color, at first because of how different the color of the cones were to the rest of the image, I had a larger range of values that I had defined as a cone. When I had this, the light and reflections from the exit signs were also flagged as cones, as they were within the range I had defined, resulting in my path running parallel across the image. I created another file that I used to find the specific values of the cones, which I used to tune the values of my mask. 

## What libraries are used##
OpenCV and numpy
