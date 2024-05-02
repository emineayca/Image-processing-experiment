import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import numpy as np

image = np.array(Image.open("C:\Users\DELL\Desktop\flutter\resimisleme.png"))


height = image.shape[0]
bottom_three_rows = image[height-3:]


text1 = pytesseract.image_to_string(bottom_three_rows)

print(text1)
