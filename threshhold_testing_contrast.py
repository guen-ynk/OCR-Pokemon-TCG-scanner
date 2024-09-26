import cv2
import numpy as np
import matplotlib.pyplot as plt

card_image_path = '...'  # Path to img

# Load Img in Grayscale
card_img_gray = cv2.imread(card_image_path, cv2.IMREAD_GRAYSCALE)

# Define Treshholds
low_thresh = 90   # everything below value stays black
high_thresh = 200  # everything above value is colored white

# create empty mask
binary_img = np.zeros_like(card_img_gray)

# set pixel above treshhold white
binary_img[card_img_gray > high_thresh] = 255

# set pixel below treshhold black
#binary_img[card_img_gray < low_thresh] = 0

# show results
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(card_img_gray, cmap='gray')
plt.title('original grayscale image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(binary_img, cmap='gray')
plt.title(f'binary image\n(low_thresh={low_thresh}, high_thresh={high_thresh})')
plt.axis('off')

plt.subplot(1,3,3)
plt.hist(card_img_gray.ravel(), bins=256, range=[0,256])
plt.axvline(low_thresh, color='r', linestyle='dashed', linewidth=1)
plt.axvline(high_thresh, color='r', linestyle='dashed', linewidth=1)
plt.title('diagram with treshhold values')
plt.show()
