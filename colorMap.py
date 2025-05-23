import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.colors import LinearSegmentedColormap

def colorGradeBGRMatPlot(ndvi,nombre,multiplo,pathproject,tipofoto):
	ndvi=ndvi*multiplo
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
	
	fig, ax = plt.subplots()
	fig.subplots_adjust(bottom=0,left=0,top=1,right=1)
	del ndvi
	im = ax.imshow(data, cmap=cmap,vmin=0,vmax=vmax)
	ax.set_axis_off()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	print "hola"
	#del cmap
	#im = ax.pcolor(data, cmap=cmap, vmin=0, vmax=vmax)
	#cbar = fig.colorbar(im, ticks=[0, 1, 2], orientation='vertical')
	#cbar.ax.set_xticklabels(['-1', '0', '1',])  # horizontal colorbar
	print "syse"
	print sys.getsizeof(im)
	print sys.getsizeof(fig)
	print sys.getsizeof(ax)
	print sys.getsizeof(data)
	#plt.show()	
	plt.savefig(pathproject+"ResultadosNDVI/ResMatPlot/"+tipofoto+nombre+"MatploTNDVI.jpg",bbox_inches='tight', pad_inches=0,dpi=200)	
	fig.clf()
	plt.close()
	
	
