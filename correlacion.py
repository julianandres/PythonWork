import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
import funciones
img1 = cv2.imread("/home/julian/PythonWork/Bandas/DobleCam/17febRGBSolBLUE.jpg") 
img2 = cv2.imread("/home/julian/PythonWork/Bandas/pruebasFiltroAzul/17febNoirBlueBLUEFilterBlueAWB11.jpg") 
result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)
print result
