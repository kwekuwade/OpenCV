import numpy as np
import cv2
import os

#Create a white canvas
def createCanvas(color, height, width):
    colorNum = [0, 0, 0]

    x = np.zeros((height, width, 3), dtype=np.uint8)

    if color == "white":
        colorNum = [255, 255, 255]

    x[:] = colorNum

    return x

# Display an image
def displayImage(window_name, image):
    cv2.imshow(window_name, image)

canvas = createCanvas("white", 300, 300)

displayImage('Canvas', canvas)

image_url = os.path.join(os.getcwd(), 'OpenCV/images/color_wheel.jpg')

colorPalette = cv2.imread(image_url)

displayImage('Canvas', colorPalette)

cv2.waitKey(0)
cv2.destroyAllWindows()