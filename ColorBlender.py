import numpy as np
import cv2
import os

#Create a white canvas
def createCanvas(color, height, width):
    x = np.zeros((height, width, 3), dtype=np.uint8)
    x[:] = color

    return x

# Display an image
def displayImage(window_name, image):
    cv2.imshow(window_name, image)

canvas = createCanvas([255, 255, 255], 300, 300)

image_url = os.path.join(os.getcwd(), 'OpenCV/images/color_wheel.jpg')
colorPalette = cv2.imread(image_url)

displayImage('Canvas', canvas)
displayImage('Color Palette', colorPalette)

cv2.waitKey(0)
cv2.destroyAllWindows()
