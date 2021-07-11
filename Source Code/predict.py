
import sys  

ind1 = sys.argv[1]
ind2 = sys.argv[2]


i1='data/test/' + str(ind1) + '.tif'
i2='preds/' + str(ind1) + '_pred.png'
i3='data/test/' + str(ind2) + '.tif'
i4='preds/' + str(ind2) + '_pred.png'

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

fig , ax = plt.subplots(2,2)

ax[0 , 0].set_title(i1)
ax[0 , 1].set_title(i2)
ax[1 , 0].set_title(i3)
ax[1 , 1].set_title(i4)

img1 = mpimg.imread(i1)
ax[0,0].imshow(img1)
img2 = mpimg.imread(i2)
ax[0,1].imshow(img2)

img1 = mpimg.imread(i3)
ax[1,0].imshow(img1)
img2 = mpimg.imread(i4)
ax[1,1].imshow(img2)

plt.show()
