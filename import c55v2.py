import cv2
import numpy as np 
resim=np.zeros((512,512,3),np.uint8)
cv2.imshow("resimadi",resim)
resim2 =cv2.line(resim(0,0),(512,512),(255,0,0),6)

cv2.imshow("resimadi",resim2)

cv2.waitKey(0)
cv2.destroyAllWindows()