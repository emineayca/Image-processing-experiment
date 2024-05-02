# Imgenin x ve y yonlerindeki turevini bul
imyg, imxg = np.gradient(sim)
plt.imshow(imxg,cmap='gray')
plt.show()

plt.imshow(imyg,cmap='gray')
plt.show()
