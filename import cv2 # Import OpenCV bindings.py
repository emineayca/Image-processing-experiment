import cv2 # Import OpenCV bindings
import numpy as np # Import NumPy
from matplotlib import pyplot as plt # Import PyPlot

def filterImage(image, kernel):
    """ Imge ile kerneli konvole et"""
    ret = image.copy() 
    size_y = image.shape[0]
    size_x = image.shape[1] 
    kernel_size = len(kernel) 
    ofs = kernel_size/2
    for i in range(ofs, size_y-ofs):
        for j in range(ofs, size_x -ofs):
            val = 0
            for k in range(kernel_size * kernel_size):
                im_val = image[i + k/kernel_size - ofs][j+ k%kernel_size-ofs]
                val += kernel[k/kernel_size][k%kernel_size] * im_val
            ret[i][j] = val
    return ret 

class GaussKernel:
    """ Gauss Kernel sinifi """
    def __init__(self, kernel_size, sigma):
        self.kernel_size = kernel_size
        self.sigma = sigma 
        self.kernel = self._createKernel()

    def _createKernel(self):
        l = (self.kernel_size - 1) // 2 
        x = np.array(range(-l,l+1)) 
        xx, yy = np.meshgrid(x,x) 
        kernel = np.exp(-1 *( np.power(xx,2) + np.power(yy,2) )/ 2.0 * np.power(self.sigma,2))
        return kernel / np.sum(kernel) 
    
    def getKernel(self):
        return self.kernel