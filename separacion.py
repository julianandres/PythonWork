
import sys
sys.path.append('/usr/lib/python2.7/site-packages')
print sys.path
import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones
base='probes/probeBands/'
nombre='23febRGBSolconAWB'
extension='.jpg'
base2='probes/probeBands/'
nombre2='23febRGBSolNoawb'
extension2='.jpg'
print base+nombre+extension
img = cv2.imread(base+nombre+extension) #banda IRRojo
print base2+nombre2+extension2
img2 = cv2.imread(base2+nombre2+extension2) #banda infraroja
base3='probes/probeBands/'
nombre3='dobleCamRGBTercero'
extension3='.jpg'
img3 = cv2.imread(base3+nombre3+extension3) #banda infraroja

IR,g,RED = cv2.split(img)
IR2,g2,RED2 = cv2.split(img2)
IR3,g3,RED3 = cv2.split(img3)
#print img.shape


#cv2.imshow("IR",RED)

img = cv2.merge((IR3.astype('uint8'),g.astype('uint8'),RED.astype('uint8')))
cv2.imwrite('imgResultante.jpg',img)

resta = RED2-RED
print resta
resta[resta<0]=0
resta[resta>255]=0
cv2.imwrite('Bandas/restaPrueba/'+nombre+'Resta.jpg',resta)

#funciones.loadImageAndNDVIFilterBlue(img,"filterBlue"+nombre)
cv2.imwrite('Bandas/restaPrueba/'+nombre+'IR.jpg',IR)
#cv2.imshow("Blue",b)	
cv2.imwrite('Bandas/restaPrueba/'+nombre+'Red.jpg',RED)
#cv2.imshow("Green",g)
cv2.imwrite("Bandas/restaPrueba/"+nombre+"Green.jpg",g)
print "hola"
cv2.imwrite('Bandas/restaPrueba/'+nombre2+'IR.jpg',IR2)
#cv2.imshow("Blue",b)	
cv2.imwrite('Bandas/restaPrueba/'+nombre2+'Red.jpg',RED2)
#cv2.imshow("Green",g)
cv2.imwrite("Bandas/restaPrueba/"+nombre2+"Green.jpg",g2)
# calculate the ndvi and get the color graded version
