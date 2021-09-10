from .plots import *
from .models import *

def make_graph(a, num):
	li = []
	for i in a:
		if(a[i]==''):
			li.append(None)
		else:
			li.append(a[i])

	if(num == 1):
		return bar_plot(df, li)

	elif(num == 2):
		return scatter_plot(df, li)

	elif(num == 3):
		return line_plot(df, li)

	elif(num == 4):
		return count_plot(df, li)

	elif(num == 5):
		return hist_plot(df, li)

	else:
		return box_plot(df, li)

def deleteGraph(graph_type):
	if(graph_type == 'Bar Plot'):
		graph = BarPlotModel.objects.get(name= graph_type)
		graph.delete()
	elif(graph_type == 'Scatter Plot'):
		graph = ScatterPlotModel.objects.get(name= graph_type)
		graph.delete()
	elif(graph_type == 'Line Plot'):
		graph = LinePlotModel.objects.get(name= graph_type)
		graph.delete()
	elif(graph_type == 'Count Plot'):
		graph = CountPlotModel.objects.get(name= graph_type)
		graph.delete()
	elif(graph_type == 'Histogram'):
		graph = HistogramPlotModel.objects.get(name= graph_type)
		graph.delete()
	else:
		graph = BoxPlotModel.objects.get(name= graph_type)
		graph.delete()