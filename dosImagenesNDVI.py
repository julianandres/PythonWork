import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones

base='probes/probeBands/'
nombre='17febRGBSol'
extension='.jpg'

base2='probes/probeBands/'
nombre2='17febNoirBlue'
extension2='.jpg'
print base+nombre+extension
img = cv2.imread(base+nombre+extension) #banda roja normal
print base2+nombre2+extension2
img2 = cv2.imread(base2+nombre2+extension2) #banda infraroja

pathproject="/home/julian/PythonWork/"

b,g,RED = cv2.split(img)
b2,g2,IR2 = cv2.split(img2)


img = cv2.merge((b.astype('uint8'),g2.astype('uint8'),IR2.astype('uint8')))
cv2.imwrite('imgResultante.jpg',img)
funciones.loadImageAndNDVIBlueFilter(img,"dosImagenes"+nombre,pathproject)

cv2.imwrite('Bandas/DobleCam/'+nombre+'RED.jpg',RED)
#cv2.imshow("Blue",b)	
cv2.imwrite('Bandas/DobleCam/'+nombre+'BLUE.jpg',b)
#cv2.imshow("Green",g)
cv2.imwrite("Bandas/DobleCam/"+nombre+"Green.jpg",g)
cv2.imwrite('Bandas/DobleCam/'+nombre2+'IR.jpg',IR2)
#cv2.imshow("Blue",b)	
cv2.imwrite('Bandas/DobleCam/'+nombre2+'VIS.jpg',b2)
#cv2.imshow("Green",g)
cv2.imwrite("Bandas/DobleCam/"+nombre2+"Green.jpg",g2)
# calculate the ndvi and get the color graded version
