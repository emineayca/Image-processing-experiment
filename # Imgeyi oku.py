# Imgeyi oku. rgb ve grayscale kopyalarini tut
filename = "blocks.jpg"
im = cv2.imread(filename)
result = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = np.array(im,dtype=np.float)

# Gauss kernel uygula
g = GaussKernel(3,.8)
kernel = g.getKernel()
sim = filterImage(im, kernel)
plt.imshow(sim,cmap='gray')
plt.show()