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
		return bar_plot(df, li, plot_image_name)

	elif(num == 2):
		return scatter_plot(df, li, plot_image_name)

	elif(num == 3):
		return line_plot(df, li, plot_image_name)

	elif(num == 4):
		return count_plot(df, li, plot_image_name)

	elif(num == 5):
		return hist_plot(df, li, plot_image_name)

	else:
		return box_plot(df, li, plot_image_name)

def deleteGraph(graph_type):
	if(graph_type == 'Bar Plot'):
		graph = BarPlotModel.objects.all()
		graph.delete()
	elif(graph_type == 'Scatter Plot'):
		graph = ScatterPlotModel.objects.all()
		graph.delete()
	elif(graph_type == 'Line Plot'):
		graph = LinePlotModel.objects.all()
		graph.delete()
	elif(graph_type == 'Count Plot'):
		graph = CountPlotModel.objects.all()
		graph.delete()
	elif(graph_type == 'Histogram'):
		graph = HistogramPlotModel.objects.all()
		graph.delete()
	else:
		graph = BoxPlotModel.objects.all()
		graph.delete()