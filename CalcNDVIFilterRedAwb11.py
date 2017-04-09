import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones

pathproject="/home/julian/PythonWork/"
base='probes/probeNDVIRedFilter/'
nombre='17febNoirSol'
extension='.jpg'
imgOriginal = cv2.imread(pathproject+base+nombre+extension)            # read next frame
b, g, r = cv2.split(imgOriginal)
#cv2.imshow('Original',imgOriginal)

#funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre)
funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre,pathproject)

#plt.show()
c = cv2.waitKey(7) % 0x100
cv2.waitKey(0)
cv2.destroyAllWindows()
#print "siguiente"

