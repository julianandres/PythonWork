import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones


base='probes/probeBands/'
nombre='23febNoirRedFilter'
extension='.jpg'
imgOriginal = cv2.imread(base+nombre+extension)            # read next frame
b, g, r = cv2.split(imgOriginal)
#cv2.imshow('Original',imgOriginal)
cv2.imwrite('original.jpg',imgOriginal)

#funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre)
funciones.loadImageAndNDVI(imgOriginal,nombre)

#plt.show()
c = cv2.waitKey(7) % 0x100
cv2.waitKey(0)
cv2.destroyAllWindows()
#print "siguiente"
