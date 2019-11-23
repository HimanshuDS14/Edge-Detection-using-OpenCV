import cv2
import numpy as np

image = cv2.imread("tom.jpg" , 0)

lap = cv2.Laplacian(image,cv2.CV_64F)

lap = np.uint8(np.absolute(lap))


sobelX = cv2.Sobel(image,cv2.CV_64F ,1,0)
sobelY = cv2.Sobel(image , cv2.CV_64F , 0 ,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))


combined = cv2.bitwise_or(sobelX , sobelY)



cv2.imshow("edges" , lap)
cv2.imshow("sobelX" ,sobelX)
cv2.imshow("sobelY" ,sobelY)
cv2.imshow("combine sobel" , combined)



cv2.imshow("image" , image)

cv2.waitKey(0)
cv2.destroyAllWindows()