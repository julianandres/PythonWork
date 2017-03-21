import sys

from os import listdir
sys.path.append('/usr/local/lib/python2.7/site-packages')
import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones

print sys.argv
pathproject=sys.argv[1]
archivosNoir=listdir(pathproject+'FotoNoir/')
archivosRGB=listdir(pathproject+"FotoRGB/")
if((len(archivosNoir)>0) and (len(archivosRGB)>0)) :
#colocar funcion de trabajo
	pathFotoRGB=pathproject+'FotoRGB'+"/"+archivosRGB[0]
	pathFotoNoir=pathproject+'FotoNoir'+"/"+archivosNoir[0]
	imgOriginal = cv2.imread(pathFotoNoir)            # read next frame
	#b, g, r = cv2.split(imgOriginal)
	#cv2.imshow('Original',imgOriginal)
	#funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,nombre)
	funciones.loadImageAndNDVIUnaImagenAWB11(imgOriginal,"prueba",pathproject)
	
	#cv2.destroyAllWindows()
	#print "siguiente"

