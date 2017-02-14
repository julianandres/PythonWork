import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import cv2



base='probes/probeBands/'
nombre='dobleCamNoirSol'
extension='.jpg'

img = cv2.imread(base+nombre+extension,0) #banda roja normal
data=img.astype('float')/255
data=data
#mask = np.tri(data.shape[0], k=-6)
#print mask
#data = np.ma.masked_where(mask, data)
print data
vmax = 1.0
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'green'),
                                                    (0.5 / vmax, 'yellow'),
                                                    (1 / vmax, 'red')]                                    
print "hola2"
fig, ax = plt.subplots()

im = ax.imshow(data, interpolation='nearest', cmap=cmap,vmin=0,vmax=vmax)
cv2.imshow("hola",im)
print "hola"
#im = ax.pcolor(data, cmap=cmap, vmin=0, vmax=vmax, edgecolors='black')
cbar = fig.colorbar(im)
print "hola3"
cbar.set_ticks(range(5)) # Integer colorbar tick locations
ax.set(frame_on=False, aspect=1, xticks=[], yticks=[])
print "hola4"
plt.show()
