import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def colorGradeBGRMatPlot(ndvi,nombre):
	ndvi=ndvi
	data=ndvi+1
	
	#mask = np.tri(data.shape[0], k=-6)
	#print mask
	#data = np.ma.masked_where(mask, data)
	
	vmax = 2.0
	cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, '#000011'),
							    (1 / vmax, '#0000AA'),
		                                            (1 / vmax, 'green'),
							    (1.5 / vmax, 'yellow'),
		                                            (2 / vmax, 'red')]
		                                )

	#cmapvals=cmap._segmentdata
	
	fig, ax = plt.subplots(figsize=(10, 10))


	im = ax.imshow(data, cmap=cmap,vmin=0,vmax=vmax)
	print "hola"
	#im = ax.pcolor(data, cmap=cmap, vmin=0, vmax=vmax)
	cbar = fig.colorbar(im, ticks=[0, 1, 2], orientation='horizontal')
	cbar.ax.set_xticklabels(['-1', '0', '1',])  # horizontal colorbar
	print "hola4"
	plt.savefig("ResultadosNDVI/ResMatPlot/"+nombre+"MatploTNDVI.png")	
	plt.show()
	
