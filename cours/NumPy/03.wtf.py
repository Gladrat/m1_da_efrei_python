import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(r".\img.jpeg")
print(img)

img = img.copy()

# img[:, :, 0] = 0

# rotated = np.transpose(img, (1, 0, 2))
# rotated = np.flipud(rotated)

r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
img_2 = 0.2989 * r + 0.5870 * g + 0.1140 * b

plt.imshow(img_2, cmap="gray")
plt.axis('off')
plt.show()

# img = np.random.rand(2, 4, 3).round(2)
# print(img)
# print(img.ndim)
# print(img.shape)

# img[0, 2, 0] = 0
# img[0, 2, 1] = 0
# img[0, 2, 2] = 0

# plt.imshow(img)
# plt.axis('off')
# plt.show()