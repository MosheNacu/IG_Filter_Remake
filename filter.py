import cv2
import numpy as np

img = cv2.imread("JapMinimalist_Nacu.png")

#resize
scale=25
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dsize = (width, height)
img = cv2.resize(img, dsize)

#apply canny edge detection
canny = cv2.Canny(img, 100, 200)

#image translation for shifted effect
t_height, t_width = height / 25, width / 25
T = np.float32([[1, 0, t_width], [0, 1, t_height]]) 
img_translation = cv2.warpAffine(canny, T, (width, height)) 

merged = np.bitwise_or(img, img_translation[:,:,np.newaxis])

#show outputs
cv2.imshow("orig", img)
cv2.imshow("edges", canny)
cv2.imshow("filter", merged)

cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()