import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones

pathproject="/home/julian/PythonWork/"
base='probes/probeNDVIRedFilter/'
nombre='mosaicYaguara2'
extension='.jpg'
imgOriginal = cv2.imread(pathproject+base+nombre+extension)            # read next frame
b, g, r = cv2.split(imgOriginal)
#cv2.imshow('Original',imgOriginal)
cv2.imwrite('original.jpg',imgOriginal)

#funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre)
funciones.loadImageAndNDVIRedFilter1054(imgOriginal,nombre,pathproject)

#plt.show()

#print "siguiente"
