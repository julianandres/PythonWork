import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones
import sys

pathproject="/home/julian/PythonWork/"
base='probes/probeNDVIRedFilter/'
nombre='mosaicoYaguara2'
extension='.jpg'
imgOriginal = cv2.imread(pathproject+base+nombre+extension)            # read next frame
#cv2.imshow('Original',imgOriginal)
cv2.imwrite('original.jpg',imgOriginal)
print sys.getsizeof(imgOriginal)
#funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre)
funciones.loadImageAndNDVIRedFilter1054(imgOriginal,nombre,pathproject)

del imgOriginal
#plt.show()

#print "siguiente"
