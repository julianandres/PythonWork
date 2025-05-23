import numpy as np
import cv2
import os
import datetime
import colorMap
from matplotlib import pyplot as plt


# Transforms the NDVI into the Blue to Green grading


def NDVICalc(original):
    "This function performs the NDVI calculation and returns an RGB frame)"
    lowerLimit = 5 #this is to avoid divide by zero and other weird stuff when color is near black

    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape; 
    ndviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    ndvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing NDVI value
    Vis = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    IR = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue
    green = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue
    #Now get the specific channels. Remember: (B , G , R)
    Vis = (original[:,:,2]).astype('float')
    IR = (original[:,:,0]).astype('float')
    green = (original[:,:,1]).astype('float')
    Vis=Vis-green
    print Vis
    print "red channel"
    #Perform NDVI calculation
    summ = Vis+IR
    diff=IR-Vis
    summ[summ<lowerLimit] = lowerLimit #do some saturation to prevent low intensity noise
    
    bottom = (Vis.astype(np.float32) + IR)
    bottom[bottom == 0] = 0.01  # Make sure we don't dMiivide by zero!

    ndvi = (IR - Vis) / bottom
    division=ndvi
    print division
    
    division=division+1
    division=division*127
    ndvi = division.astype('uint8')
    print ndvi
    print "ndviLab"
    redSat = (ndvi-128)*2  #red channel
    bluSat = ((255-ndvi)-128)*2 #blue channel
    redSat[ndvi<128] = 0; #if the NDVI is negative, no red info
    bluSat[ndvi>=128] = 0; #if the NDVI is positive, no blue info


    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    ndviImage[:,:,2] = redSat

    #Blue Channel
    ndviImage[:,:,0] = bluSat

    #Green Channel
    ndviImage[:,:,1] = 255-(bluSat+redSat)

    return ndviImage;

def colorGradeBG(ndvi):

	# red channel
    red = np.zeros(ndvi.shape,np.float32)

    # blue channel
    blue = cv2.divide(ndvi, 2)
    blue = cv2.subtract(0.5, blue)

    # green channel
    green = cv2.add(ndvi, 1.0)
    green = cv2.divide(green, 2.0)

    gradedNDVI = cv2.merge((blue,green,red))
    return gradedNDVI

def colorGradeBGR(ndvi):
    
    maskGreater = cv2.compare(ndvi, 0.0, cv2.CMP_GE)
    cv2.imwrite('mkGreater.jpg',maskGreater)
    maskLess = cv2.compare(ndvi, 0.0, cv2.CMP_LT)
    cv2.imwrite('mkLess.jpg',maskLess)

    ## greater than 0 part
    # red
    
    red = np.zeros(ndvi.shape,np.float32)#
    
    # blue is 0
    blue = cv2.add(red,0.0, mask = maskGreater) #, dtype=np.float32)
    
    # red
    #red = cv2.add(ndvi,0.0, mask = maskGreater)
    red = cv2.multiply(ndvi,1.7)
    print "redGrade"
    #print red
    # green
    green = cv2.subtract(2.0, red, mask = maskGreater)

    ## less than 0 part

    # red is 0

  	# blue
    blue = cv2.add(blue, 4.0, mask = maskLess)
   
    # green
    lowgreen = cv2.add(ndvi,1.5, mask = maskLess)
    green = cv2.add(green, lowgreen)
   
    # clamp to [0,1]
    red = cv2.min(red,1)
    red = cv2.max(red,0)  
  
    green = cv2.min(green,1)
    green = cv2.max(green,0)   
    blue = cv2.min(blue,1)
    blue = cv2.max(blue,0) 
    gradedNDVI = cv2.merge((blue,green,red))
    return gradedNDVI


# calculates the NDVI from 2 red images
# Frames have to be aligned
def calculateNDVI(VISframe, IRframe, grading,original,nombre):
    
    
    # convert to floating point precision and scale down to [0;1]
    fVIS = VISframe.astype(np.float32)
    #fBLUE = cv2.divide(fBLUE, 255.0)
    #print fBLUE
    fIR = IRframe.astype(np.float32)
    #fIR = cv2.divide(fIR, 255.0)
    # calc the ndvi equation
    numerator = fIR-fVIS
    #numerator = fIR-fBLUE
    #print numerator
    denumerator = fIR+fVIS
    denumerator[denumerator == 0] = 1
    fraction = numerator/denumerator
    print "ndviProbeuno"
    print fraction
    print "ndviProbeuno"
    NDVIframe = fraction
    #NDVIframe = ndvi
    #cv2.imshow('NDVImetodo2',NDVIframe)
    #cv2.imwrite('NDVImetodo2.jpg',NDVIframe)
    fraction=0
    fVIS=0
    fIR=0
    VISframe=0
    IRframe=0
    numerator=0
    denumerator=0
    original=0
    

    # apply additional grading
    if grading == "BG":
    	print "BG"
        NDVIframeG = colorGradeBG(NDVIframe)
    elif grading == "BGR":
    	print "BGR"
        NDVIframeG = colorGradeBGR(NDVIframe)
    else:
    	print "NO"
        #NDVIframeG = NDVIframe

    
    return NDVIframe, NDVIframe

def loadImageAndNDVIRedFilter1054(img,nombre,pathproject):
	print "IMGAnDNDVI"

	IR,g,RED = cv2.split(img)
	#print img.shape
        #IR = cv2.equalizeHist(IR)
	cv2.imwrite('Bandas/'+nombre+'REDPrev.jpg',RED)

	RED = (2.36*(RED.astype('int'))-1.3*(g.astype('int')))
	RED=RED*0.99
	#RED = (2.42*(RED.astype('int'))-2.3*(IR.astype('int')))
	#RED=RED*0.97
	
	img = cv2.merge((IR.astype('int'),g.astype('int'),RED.astype('int')))
	cv2.imwrite('ResultantesNGB/'+nombre+'imgResultanteFilterRedAWB1054.jpg',img)
	
	cv2.imwrite('Bandas/pruebasFiltroRojo/'+nombre+'IRFilterRedAWB1054.jpg',IR)
	#cv2.imshow("Blue",b)	
	cv2.imwrite('Bandas/pruebasFiltroRojo/'+nombre+'REDFilterRedAWB1054.jpg',RED)
	#cv2.imshow("Green",g)
	cv2.imwrite("Bandas/pruebasFiltroRojo/"+nombre+"GreenFilterRedAWB1054.jpg",g)
	# show the results
	#cv2.imshow("NDVI",ndvi1)
	#cv2.imshow("NDVI2",ndvi2)
	ndvi1, ndvi2 = calculateNDVI(RED,IR,"NO",img,nombre)
	del img,IR,g,RED,ndvi2
	img=False
	IR=False
	g=False
	RED=False
	ndvi2=False
	print "free memory"
	colorMap.colorGradeBGRMatPlot(ndvi1,nombre,1,pathproject,"FilterRedAWB1054")
	img1 = cv2.imread("/home/julian/PythonWork/Bandas/DobleCam/17febRGBSolRED.jpg") 
	img2 = cv2.imread("/home/julian/PythonWork/Bandas/pruebasFiltroRojo/17febNoirSolREDFilterRedAWB1054.jpg") 
	result = cv2.matchTemplate(img2,img1,cv2.TM_CCOEFF_NORMED)
	print result
	
	#cv2.imshow("COLORMAP",img_map)
	# write to disc
        print "writing Images"

def loadImageAndNDVIUnaImagenAWB11(img,nombre,pathproject):
	print "IMGAnDNDVI"
	
	IR,g,RED = cv2.split(img)
	#print img.shape
        IR = IR
	cv2.imwrite(pathproject+'Bandas/'+nombre+'REDPrevFilterRedAWB11.jpg',RED)
	RED=RED.astype('int')
	RED=RED*0.56
	RED = 2.3*(RED)-1.6*(g.astype('int'))
	#RED = cv2.equalizeHist(RED)
	
	
	#RED = cv2.equalizeHist(RED)*0.4
	print "redprevio"
	
	#cv2.imshow("IR",RED)
	
	img = cv2.merge((IR.astype('int'),g.astype('int'),RED.astype('int')))
	cv2.imwrite(pathproject+'ResultantesNGB/'+nombre+'imgResultanteFilterRedAWB11.jpg',img)
	
	cv2.imwrite(pathproject+'Bandas/pruebasFiltroRojo/'+nombre+'IRFilterRedAWB11.jpg',IR)
	#cv2.imshow("Blue",b)	
	cv2.imwrite(pathproject+'Bandas/pruebasFiltroRojo/'+nombre+'REDFilterRedAWB11.jpg',RED)
	#cv2.imshow("Green",g)
	cv2.imwrite(pathproject+"Bandas/pruebasFiltroRojo/"+nombre+"GreenFilterRedAWB11.jpg",g)
	# calculate the ndvi and get the color graded version11
	ndvi1, ndvi2 = calculateNDVI(RED,IR,"NO",img,nombre)
	del img,IR,g,RED,ndvi2
	print "delete memory"

	colorMap.colorGradeBGRMatPlot(ndvi1,nombre,1,pathproject,"FilterRedAWB11")

	img1 = cv2.imread("/home/julian/PythonWork/Bandas/DobleCam/17febRGBSolRED.jpg") 
	img2 = cv2.imread("/home/julian/PythonWork/Bandas/pruebasFiltroAzul/17febNoirREDFilterRedAWB11.jpg") 
	result = cv2.matchTemplate(img2,img1,cv2.TM_CCOEFF_NORMED)
	print result
	# scale the NDVI from [-1;1] to [0;1] for propper display
	print "finalizadoNDVI"


def loadImageAndNDVIFilterBlueAWB11(img,nombre,pathproject):
	print "IMGAnDNDVI"
	
	blue,g,IR = cv2.split(img)
	#print img.shape
        #IR = cv2.equalizeHist(IR)
	
	#RED = cv2.equalizeHist(RED)
	print blue
	print IR
	blue=(blue.astype('int')*1.7-1.3*IR.astype('int'))+3
	blue[blue<0]=0
	print blue
	#IR=IR*0.8
	blue = blue*3.2
	print "redprevio"
	
	#cv2.imshow("IR",RED)
	
	img = cv2.merge((blue.astype('int'),g.astype('int'),IR.astype('int')))
	cv2.imwrite('ResultantesNGB/DobleCam/'+nombre+'imgResultanteFilterBlueAWB11.jpg',img)

	# calculate the ndvi and get the color graded version
	ndvi1, ndvi2 = calculateNDVI(blue,IR,"BGR",img,nombre)
	colorMap.colorGradeBGRMatPlot(ndvi1,nombre,0.8,pathproject,"FilterBlueAWB11")
	#	cv2.imwrite('Bandas/'+nombre+'REDPrev.jpg',blue)
	cv2.imwrite('Bandas/pruebasFiltroAzul/'+nombre+'IRFilterBlueAWB11.jpg',IR)
	#cv2.imshow("Blue",b)	
	cv2.imwrite('Bandas/pruebasFiltroAzul/'+nombre+'BLUEFilterBlueAWB11.jpg',blue)
	#cv2.imshow("Green",g)
	cv2.imwrite("Bandas/pruebasFiltroAzul/"+nombre+"GreenFilterBlueAWB11.jpg",g)
	img1 = cv2.imread("/home/julian/PythonWork/Bandas/DobleCam/17febRGBSolBLUE.jpg") 
	img2 = cv2.imread("/home/julian/PythonWork/Bandas/pruebasFiltroAzul/17febNoirBlueBLUEFilterBlueAWB11.jpg") 
	result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)
	print result
	
	
	print "finalizadoNDVI"               
def loadImageAndNDVIBlueFilter(img,nombre,pathproject):
	print "IMGAnDNDVI"
	
	blue,g,IR = cv2.split(img)
	#print img.shape
        #IR = cv2.equalizeHist(IR)
	#cv2.imshow("IR",RED)
	
	img = cv2.merge((blue.astype('int'),g.astype('int'),IR.astype('int')))
	cv2.imwrite('ResultantesNGB/DobleCam/'+nombre+'imgResultanteFilterBlueAWB11.jpg',img)

	# calculate the ndvi and get the color graded version
	ndvi1, ndvi2 = calculateNDVI(blue,IR,"BGR",img,nombre)
	colorMap.colorGradeBGRMatPlot(ndvi1,nombre,0.8,pathproject,"DobleCamera")
	
	
	print "finalizadoNDVI"   
def loadImageAndNDVIRedFilter(img,nombre,pathproject):
	print "IMGAnDNDVI"
	
	IR,g,r = cv2.split(img)
	#print img.shape
        #IR = cv2.equalizeHist(IR)
	#cv2.imshow("IR",RED)
	
	img = cv2.merge((IR.astype('int'),g.astype('int'),r.astype('int')))
	cv2.imwrite('ResultantesNGB/'+nombre+'imgResultanteFilterRedAWB11.jpg',img)

	# calculate the ndvi and get the color graded version
	ndvi1, ndvi2 = calculateNDVI(r,IR,"NO",img,nombre)
	colorMap.colorGradeBGRMatPlot(ndvi1,nombre,1,pathproject,"DobleCamera")
	#	cv2.imwrite('Bandas/'+nombre+'REDPrev.jpg',Red)
	cv2.imwrite('Bandas/pruebasFiltroRojo/'+nombre+'IRFilterRedAWB11.jpg',r)
	#cv2.imshow("Red",b)	
	cv2.imwrite('Bandas/pruebasFiltroRojo/'+nombre+'redFilterRedAWB11.jpg',IR)
	#cv2.imshow("Green",g)
	cv2.imwrite("Bandas/pruebasFiltroRojo/"+nombre+"GreenFilterRedAWB11.jpg",g)
	# scale the NDVI from [-1;1] to [0;1] for propper display
	ndvi1 = cv2.add(ndvi1, 1.0)
	ndvi1 = cv2.divide(ndvi1, 2.0)
	
	# show the results
	cv2.imshow("NDVI",ndvi1)
	cv2.imshow("NDVI2",ndvi2)

	#transpose to [0;255] to save as 8bit
	ndvi1 = cv2.multiply(ndvi1, 255)

	ndvi2 = cv2.multiply(ndvi2, np.array([255.0,255.0,255.0,0.0]))
	#print "ndvi2"
	#print ndvi1
	
	# convert back to 8bit
	intNDVI = ndvi1.astype(np.uint8)
	intNDVI2 = ndvi2.astype(np.uint8)
	
	print "finalizadoNDVI"   

