import numpy as np
import cv2
import pytesseract

# kernel of dilation
kernel = np.ones((3, 21),np.uint8)

# read image
img = cv2.imread('image.jpg')	# path to your image

# resize image
img = cv2.resize(img, (900, 600))
img_ori = img.copy()

# change to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# dilate image
img_dilate = cv2.erode(img_gray,kernel,iterations = 1)

# binary image
img_binary = cv2.Canny(img_dilate, 80, 255)

# find contourss
contours, _ = cv2.findContours(img_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2) 

# save result image
cv2.imwrite('contours.jpg', img)

# get the boxes
contour_list = []

margin = 15

for c in contours:
	(x, y, w, h) = cv2.boundingRect(c)
	if (w>30 and h >30):
		curr_image = img_ori[y-margin:y+h+margin,x-margin:x+w+margin]  
		cv2.imshow('curr_image', curr_image)
		cv2.waitKey()
		print(pytesseract.image_to_string(curr_image, lang='vie'))
