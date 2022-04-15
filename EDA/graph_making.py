from .plots import *
from .models import *

def make_graph(a, num, plot_image_name):
	li = []
	for i in a:
		if(a[i]==''):
			li.append(None)
		else:
			li.append(a[i])

	if(num == 1):
		return bar_plot(li, plot_image_name)

	elif(num == 2):
		return scatter_plot(li, plot_image_name)

	elif(num == 3):
		return line_plot(li, plot_image_name)

	elif(num == 4):
		return count_plot(li, plot_image_name)

	elif(num == 5):
		return hist_plot(li, plot_image_name)

	else:
		return box_plot(li, plot_image_name)