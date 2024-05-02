import opencv  
import numpy as np
# Resmi yükle
image = cv2.imread('resimisleme.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Harris köşe tespiti için parametreleri ayarla
harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Eşik değeri seç
threshold = 0.01 * harris_corners.max()

# Köşe noktalarını bul
corner_image = np.copy(image)
corner_image[harris_corners > threshold] = [0, 0, 255]

# Sonuçları göster
cv2.imshow('Corner Image', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
