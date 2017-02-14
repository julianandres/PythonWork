import time
import numpy as np
from matplotlib import pyplot as plt
import cv2

base='probes/probeBands/'
nombre='separarStream'
extension='.png'
print base+nombre+extension
img = cv2.imread(base+nombre+extension)   
IR,g,RED = cv2.split(img)
#print img.shape
print RED
cv2.imwrite('Bandas/'+nombre+'REDPrev.jpg',RED)
IR = IR
RED = cv2.equalizeHist(RED)
RED[RED<0] = 0
print "redprevio"

#cv2.imshow("IR",RED)

img = cv2.merge((IR.astype('uint8'),g.astype('uint8'),RED.astype('uint8')))
cv2.imwrite('imgResultante.jpg',img)

cv2.imwrite('Bandas/'+nombre+'IR.jpg',IR)
#cv2.imshow("Blue",b)	
cv2.imwrite('Bandas/'+nombre+'RED.jpg',RED)
#cv2.imshow("Green",g)
cv2.imwrite("Bandas/"+nombre+"Green.jpg",g)
# calculate the ndvi and get the color graded version
