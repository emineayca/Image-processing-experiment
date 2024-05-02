import cv2 
import numpy as np    
resim =cv2.imread("resimisleme.png",0)

resim2= cv2.rectangle(resim,(15,15),(55,187),(0,255,0),7)
cv2.imshow("ödev",resim2)


cv2.waitKey(0)
cv2.destroyAllWindows()

