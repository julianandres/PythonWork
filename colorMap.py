import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.colors import LinearSegmentedColormap

def colorGradeBGRMatPlot(ndvi,nombre,multiplo,pathproject,tipofoto):
	ndvi=ndvi*multiplo
	data=ndvi+1
	vmax = 2.0
	cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, '#000011'),
							    (1 / vmax, '#0000AA'),
		                                            (1 / vmax, 'green'),
							    (1.5 / vmax, 'yellow'),
		                                            (2 / vmax, 'red')]
		                                )
	fig, ax = plt.subplots(figsize=(15,15))
	fig.subplots_adjust(bottom=0,left=0,top=1,right=1)
	del ndvi
	ndvi=False
	im = ax.imshow(data, cmap=cmap,vmin=0,vmax=vmax)
	ax.set_axis_off()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	print sys.getsizeof(data)
	print "guardando"	
	plt.savefig(pathproject+"ResultadosNDVI/ResMatPlot/"+tipofoto+nombre+"MatploTNDVI.jpg",bbox_inches='tight', pad_inches=0,dpi=230)	
	fig.clf()
	plt.close()
	
	
