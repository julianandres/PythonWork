import time
import numpy as np
from matplotlib import pyplot as plt
import cv2

base='probes/'
nombre='yaguara3'
extension='.jpg'
original = cv2.imread(base+nombre+extension)            # read next frame
b, g, r = cv2.split(original)
#cv2.imshow('Original',imgOriginal)
cv2.imwrite('original.jpg',original)
color = ('b','g','r')


"This function performs the NDVI calculation and returns an RGB frame)"
lowerLimit = 5 #this is to avoid divide by zero and other weird stuff when color is near black

awbdeseado=1
awbactual=1
multiplicador=awbdeseado/awbactual

#First, make containers
oldHeight,oldWidth = original[:,:,0].shape; 
ndviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
ndvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing NDVI value
red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue

#format hsv
h = np.ones((oldHeight,oldWidth),np.float) #make a blank array for red
s = np.ones((oldHeight,oldWidth),np.float) #make a blank array for blue
v = np.ones((oldHeight,oldWidth),np.float) #make a blank array for red

#Now get the specific channels. Remember: (B , G , R)
red = r.astype('float')-g
blue = b.astype('float')
green = g.astype('float')

#print red
blue = blue
print "red channel"
#Perform NDVI calculation
numerator = blue-red
#numerator = fIR-fBLUE

img = cv2.merge((blue.astype('int'),green.astype('int'),red.astype('int')))
cv2.imwrite('transformada.jpg',img)

#print numerator
img_HSV = cv2.cvtColor(original,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_HSV)
cv2.imwrite("red.jpg",red)
cv2.imwrite("blue.jpg",blue)
denumerator = cv2.add(red,blue)
denumerator[denumerator<lowerLimit] = lowerLimit
fraction = cv2.divide(numerator, denumerator)
print fraction
ndvi = fraction+1
#print v
#print s
h = (ndvi*180).astype(np.uint)
print h
s.fill(255)
v.fill(255)
print "hsv"

img_HSV[:,:,0]=h
img_HSV[:,:,1]=s
img_HSV[:,:,2]=v

img_RGB = cv2.cvtColor(img_HSV,cv2.COLOR_HSV2BGR)
#print img_RGB[:,:,0]
cv2.imshow('NDVIHsv',img_RGB)
cv2.imwrite("ndvihsv.jpg",img_RGB)

c = cv2.waitKey(7) % 0x100
cv2.waitKey(0)
cv2.destroyAllWindows()
