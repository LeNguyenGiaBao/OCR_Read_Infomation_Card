import cv2
import numpy as np
import pytesseract

# Read image
im = cv2.imread("image.jpg")
im = cv2.resize(im, (800, 600))

# Select ROI
while True:
    r = cv2.selectROI(im)
    
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    text = pytesseract.image_to_string(imCrop, lang='vie')
    print(text)