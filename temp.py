
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh 
from skimage.color import rgb2gray
from skimage.io import * 

import numpy as np
import matplotlib.pyplot as plt 

img1 = data.hubble_deep_field()[0:500,0:500]
img1 = rgb2gray(img1)

#img1 = imread('sunflower.jpg')
#img1 = rgb2gray(img1) 

img2 = imread('p2.jpg')
img2 = rgb2gray(img2)

img3 = imread('p3.jpg')
img3 = rgb2gray(img3)


blob_log = blob_log(img1, max_sigma = 30, num_sigma= 10, threshold=.2)
blob_log[:,2] = blob_log[:,2] *sqrt(2)



fig, axes = plt.subplots(1,3,figsize = (9,3) , sharex = True, sharey = True)

ax = axes.ravel() 

ax[0].set_title('LoG filter with puppy image') 
ax[0].imshow(img1, interpolation = 'nearest')


for blob in blob_log:

	y,x,r = blob
	c = plt.Circle((x,y), r, color = 'yellow', linewidth = 2, fill = False)
	ax[0].add_patch(c)
	

ax[0].set_axis_off()


plt.show()
