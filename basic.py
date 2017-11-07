
import numpy as np
import matplotlib.pyplot as plt

from skimage import color 
from skimage.data import camera
from skimage.filters import roberts, sobel, scharr, prewitt 
from skimage.io import *

image = camera() 
img = imread('p1.png')

#make image gray-scale 
img = color.rgb2gray(img)



# Apply filter on image 
edge_sobel = sobel(img)
edge_roberts = roberts(img) 

print edge_sobel



fig , ax = plt.subplots(ncols = 2, sharex = True, sharey = True ,
			figsize = (8,4))

ax[0].imshow(edge_roberts)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel)
ax[1].set_title('Sobel Edge Detection') 

plt.show()

'''
edge_roberts = roberts(image)
edge_sobel  = sobel(image)

fig , ax = plt.subplots(ncols = 2 , sharex = True, sharey = True,
			figsize=(8,4))


ax[0].imshow(edge_roberts, cmap = plt.cm.gray)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel, cmap = plt.cm.gray)
ax[1].set_title('Sobel Edge Detection') 


for a in ax:
	a.axis('off')


plt.tight_layout()
plt.show()

'''


