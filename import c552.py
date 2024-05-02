import cv2
import numpy as np
from matplotlib import pyplot as plt         
resim=cv2.imread("resimisleme.png",0)
plt.imshow(resim, cmap="gray", interpolation="bicubic")
plt.xticks([])
plt.yticks([])
plt.show()