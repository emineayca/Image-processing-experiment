import cv2
import numpy as np 
resim=cv2.imread("resimisleme.png",0)
cv2.imshow("ödev",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()